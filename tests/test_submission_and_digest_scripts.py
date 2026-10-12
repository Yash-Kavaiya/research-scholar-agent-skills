import datetime

import matplotlib

matplotlib.use("Agg")

import scholarly_api as api
from conftest import load_script

pdf = load_script("camera-ready-checker", "check_pdf")
digest = load_script("weekly-paper-digest", "digest")


# ------------------------------------------------------------------ check_pdf

def test_page_size_name():
    assert pdf.page_size_name(612, 792) == "letter"
    assert pdf.page_size_name(595.3, 841.9) == "a4"
    assert pdf.page_size_name(500, 700) == "custom (500 x 700 pt)"


def test_find_references_page_needs_a_heading_on_its_own_line():
    pages = ["Intro. See the references for details.", "5 Conclusion\ntext\nReferences\n[1] A. Author", "more refs"]
    assert pdf.find_references_page(pages) == 2
    assert pdf.find_references_page(["no heading here"]) is None
    assert pdf.find_references_page(["7. Bibliography\n[1] ..."]) == 1


def test_anonymity_findings_cover_each_leak_type():
    pages = ["In our previous work we used this. Code: https://github.com/janedoe/project and "
             "https://anonymous.4open.science/r/abc. Contact jane@example.edu.",
             "Acknowledgments\nWe thank Example University."]
    findings = pdf.anonymity_findings(pages, {"author": "Jane Doe", "title": "A Paper"}, ["Jane Doe", "Example University"])
    kinds = sorted({f["kind"] for f in findings})
    assert kinds == ["acknowledgements section", "email address", "first-person self-reference", "listed name",
                     "listed name in metadata author", "metadata author", "repository link"]
    repos = [f["text"] for f in findings if f["kind"] == "repository link"]
    assert repos == ["github.com/janedoe/project"]            # the anonymised link is not flagged


def test_anonymous_metadata_and_clean_text_pass():
    assert pdf.anonymity_findings(["Prior work by Doe et al. showed this."], {"author": "Anonymous Authors"}, []) == []


def make_pdf(path, fonttype, pages=2, author="Jane Doe"):
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages

    with matplotlib.rc_context({"pdf.fonttype": fonttype}):
        with PdfPages(path, metadata={"Author": author, "Title": "Test Paper"}) as out:
            for number in range(pages):
                fig = plt.figure(figsize=(8.5, 11))
                fig.text(0.1, 0.9, "References" if number == pages - 1 else f"Section {number + 1}")
                out.savefig(fig)
                plt.close(fig)


def test_check_reads_real_pdf_and_flags_type3_fonts_and_page_limit(tmp_path):
    good = tmp_path / "good.pdf"
    make_pdf(str(good), 42, pages=2)
    result = pdf.check(str(good), max_pages=2, paper="letter")
    assert result["pages"] == 2 and result["page_sizes"] == ["letter"]
    assert result["metadata"]["author"] == "Jane Doe"
    assert all(f["embedded"] and f["subtype"] != "Type3" for f in result["fonts"]) and result["fonts"]
    assert result["passed"]

    bad = tmp_path / "bad.pdf"
    make_pdf(str(bad), 3, pages=3)
    result = pdf.check(str(bad), max_pages=1, paper="a4", anonymous=True)
    assert not result["passed"]
    text = " | ".join(result["problems"])
    assert "Type 3 fonts present" in text and "expected a4" in text and "over the limit of 1" in text
    assert any(f["kind"] == "metadata author" for f in result["anonymity"])


# --------------------------------------------------------------------- digest

TODAY = datetime.date(2026, 3, 9)
CUTOFF = TODAY - datetime.timedelta(days=7)


def paper(pid, title, published, abstract="", source="arxiv", doi=""):
    return api.make_paper(id=pid, title=title, published=published, abstract=abstract, source=source, doi=doi,
                          authors=["A. Author"])


def test_is_recent():
    assert digest.is_recent(paper("1", "t", "2026-03-05"), CUTOFF, TODAY)
    assert not digest.is_recent(paper("1", "t", "2026-02-20"), CUTOFF, TODAY)
    assert not digest.is_recent(paper("1", "t", ""), CUTOFF, TODAY)
    assert not digest.is_recent(paper("1", "t", "2029-05-06"), CUTOFF, TODAY)   # future-dated index record


def test_select_new_filters_old_and_seen_and_ranks_by_query_hits_then_boost():
    both = paper("a", "Found by both queries", "2026-03-04")
    boosted = paper("b", "A new benchmark for X", "2026-03-06")
    plain = paper("c", "Plain recent paper", "2026-03-08")
    old = paper("d", "Old paper", "2026-01-01")
    seen_paper = paper("e", "Already reported", "2026-03-07")
    result = digest.select_new({"q1": [both, boosted, old, seen_paper], "q2": [both, plain]},
                               seen={"arxiv:e"}, cutoff=CUTOFF, boost=["benchmark"], today=TODAY)
    assert [p["id"] for p in result] == ["a", "b", "c"]
    assert result[0]["queries"] == ["q1", "q2"] and result[1]["boost_hits"] == ["benchmark"]


def test_select_new_merges_the_same_paper_from_two_sources():
    arxiv = paper("2603.00001", "Same Paper Title", "2026-03-05", source="arxiv")
    openalex = paper("W1", "Same paper title.", "2026-03-05", source="openalex", doi="10.1/x")
    result = digest.select_new({"q1": [arxiv], "q2": [openalex]}, set(), CUTOFF, today=TODAY)
    assert len(result) == 1 and result[0]["queries"] == ["q1", "q2"]


def test_render_lists_papers_and_failed_sources():
    papers = digest.select_new({"q1": [paper("a", "Title A", "2026-03-04", abstract="x" * 500)]}, set(), CUTOFF, today=TODAY)
    text = digest.render(papers, ["q1"], 7, TODAY, {"openalex": "HTTP 503"})
    assert text.startswith("# Paper digest: 2026-03-02 to 2026-03-09")
    assert "## 1. Title A" in text and "openalex: HTTP 503" in text and "x" * 400 + "…" in text
    assert "No new papers" in digest.render([], ["q1"], 7, TODAY, {})
