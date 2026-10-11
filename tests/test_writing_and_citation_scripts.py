import matplotlib

matplotlib.use("Agg")

import pytest
import scholarly_api as api
from conftest import load_script

bib = load_script("bibtex-manager", "clean_bibtex")
verifier = load_script("citation-verifier", "verify_citations")
sim = load_script("plagiarism-and-paraphrase-checker", "similarity")
tables = load_script("latex-table-generator", "csv_to_booktabs")
style = load_script("publication-figure-maker", "pubstyle")

BIB = r"""
@string{nips = "Advances in Neural Information Processing Systems"}
@comment{exported by a reference manager}
@InProceedings{vaswani,
  Author = {Vaswani, Ashish and Shazeer, Noam},
  Title = "Attention Is All You Need",
  booktitle = nips # " 30",
  Year = 2017,
  pages = {5998-6008},
  abstract = {The dominant sequence transduction models ...},
  url = {https://doi.org/10.5555/3295222.3295349},
  doi = {https://doi.org/10.5555/3295222.3295349}
}
@article{dup, title={Attention is all you need}, year={2017}, author={A. Vaswani}, journal={arXiv preprint arXiv:1706.03762}, volume={1}, number={2}, note={x}, month={jun}, publisher={y}, eprint={1706.03762}}
@article{devlin, title={BERT: Pre-training of Deep Bidirectional Transformers for mRNA and ImageNet}, author={Devlin, Jacob and others}, year={2019}}
"""


# ------------------------------------------------------------- BibTeX parsing

def test_parse_bibtex_handles_macros_quotes_concatenation_and_comments():
    entries = api.parse_bibtex(BIB)
    assert [e["key"] for e in entries] == ["vaswani", "dup", "devlin"]
    first = entries[0]
    assert first["type"] == "inproceedings"
    assert first["fields"]["booktitle"] == "Advances in Neural Information Processing Systems 30"
    assert first["fields"]["year"] == "2017" and first["fields"]["title"] == "Attention Is All You Need"


def test_parse_bibtex_keeps_nested_braces_and_latex():
    (entry,) = api.parse_bibtex(r'@article{k, title={Schr{\"o}dinger and the {$\alpha$} cat}, author={Erwin Schr{\"o}dinger}}')
    assert entry["fields"]["title"] == r'Schr{\"o}dinger and the {$\alpha$} cat'
    assert api.surname(entry["fields"]["author"]) == "schrodinger"


def test_bib_authors_and_surname():
    names = api.bib_authors("Vaswani, Ashish and Noam Shazeer and {Google Brain Team}")
    assert names == ["Vaswani, Ashish", "Noam Shazeer", "{Google Brain Team}"]
    assert [api.surname(n) for n in names] == ["vaswani", "shazeer", "google brain team"]


def test_format_bibtex_roundtrips():
    entries = api.parse_bibtex(BIB)
    assert api.parse_bibtex(api.format_bibtex(entries)) == entries


# -------------------------------------------------------------- clean_bibtex

def cleaned():
    return [bib.clean_entry(e, {"abstract", "file", "keywords"}) for e in api.parse_bibtex(BIB)]


def test_clean_entry_normalizes_fields():
    first = cleaned()[0]["fields"]
    assert first["doi"] == "10.5555/3295222.3295349"
    assert "url" not in first and "abstract" not in first
    assert first["pages"] == "5998--6008"


def test_protect_title_braces_only_inner_capitals():
    assert bib.protect_title("BERT: Pre-training of Deep Transformers for mRNA and ImageNet") == \
        "{BERT}: Pre-training of Deep Transformers for {mRNA} and {ImageNet}"
    assert bib.protect_title("Already {BERT} protected") == "Already {BERT} protected"
    assert bib.protect_title(r"The $O(N)$ bound and \LaTeX") == r"The $O(N)$ bound and \LaTeX"


def test_merge_duplicates_keeps_fuller_entry_and_maps_keys():
    entries, mapping = bib.merge_duplicates(cleaned())
    assert [e["key"] for e in entries] == ["vaswani", "devlin"]
    assert mapping == {"dup": "vaswani"}
    merged = entries[0]["fields"]
    assert merged["eprint"] == "1706.03762"                 # from the fuller duplicate
    assert merged["doi"] == "10.5555/3295222.3295349"       # kept from the first entry


def test_check_entry_reports_missing_fields_preprints_and_others():
    problems = {e["key"]: bib.check_entry(e) for e in cleaned()}
    assert problems["vaswani"] == []
    assert any("preprint" in p for p in problems["dup"])
    assert "missing journal" in problems["devlin"]


def test_rekey_generates_keys_and_resolves_collisions():
    entries = [{"type": "article", "key": "x", "fields": {"author": "Vaswani, A.", "year": "2017", "title": "Attention Is All"}},
               {"type": "article", "key": "y", "fields": {"author": "A. Vaswani", "year": "2017", "title": "The Attention Paper"}}]
    assert bib.rekey(entries) == {"x": "vaswani2017attention", "y": "vaswani2017attentionb"}


# ----------------------------------------------------------- verify_citations

RECORD = api.make_paper(title="Attention Is All You Need", authors=["Ashish Vaswani", "Noam Shazeer"], year=2017,
                        doi="10.5555/3295222.3295349", source="crossref")


def entry(**fields):
    return {"type": "article", "key": "k", "fields": fields}


def test_compare_accepts_matching_entry_and_tolerates_one_year_offset():
    assert verifier.compare(entry(title="Attention is all you need", author="Vaswani, Ashish", year="2018"), RECORD) == []


def test_compare_reports_each_disagreement():
    problems = verifier.compare(entry(title="Attention Is All You Need", author="Hinton, Geoffrey", year="2012"), RECORD)
    assert len(problems) == 2
    assert problems[0].startswith("year differs") and "Hinton" in problems[1]


def test_classify_statuses():
    good = entry(title="Attention Is All You Need", author="Vaswani, Ashish", year="2017")
    assert verifier.classify(good, RECORD, [])["status"] == "verified"
    assert verifier.classify(good, None, [RECORD])["status"] == "verified"
    wrong_year = entry(title="Attention Is All You Need", author="Vaswani, Ashish", year="2010")
    assert verifier.classify(wrong_year, RECORD, [])["status"] == "mismatch"
    loose = entry(title="Attention Is All You Need for Speech", author="Vaswani, A.", year="2017")
    assert verifier.classify(loose, None, [RECORD])["status"] == "possible_match"
    fake = entry(title="Quantum Blockchain Synergies in Medieval Agriculture", author="Nobody, N.", year="2021")
    result = verifier.classify(fake, None, [RECORD])
    assert result["status"] == "not_found" and result["matched"] is None


def test_verify_flags_fabricated_and_bad_doi_entries(monkeypatch):
    fake = {"type": "article", "key": "fake", "fields": {"title": "Quantum Blockchain Synergies", "author": "N. Nobody"}}
    bad_doi = {"type": "article", "key": "baddoi", "fields": {"title": "Attention Is All You Need",
                                                               "author": "Vaswani, Ashish", "doi": "10.1/nope"}}
    lookups = {"fake": (None, [], []), "baddoi": (None, [RECORD], ["DOI 10.1/nope was not found in Crossref or OpenAlex"])}
    monkeypatch.setattr(verifier, "lookup", lambda e: lookups[e["key"]])
    results = {r["key"]: r for r in verifier.verify([fake, bad_doi])}
    assert results["fake"]["status"] == "not_found"
    assert results["baddoi"]["status"] == "mismatch"


def test_verify_does_not_call_an_outage_a_missing_paper(monkeypatch):
    monkeypatch.setattr(verifier, "lookup", lambda e: (None, [], ["Crossref search failed: HTTP 503"]))
    (result,) = verifier.verify([entry(title="Anything")])
    assert result["status"] == "lookup_failed"


def test_arxiv_id_detection():
    assert verifier.arxiv_id({"eprint": "1706.03762v5"}) == "1706.03762"
    assert verifier.arxiv_id({"journal": "arXiv preprint arXiv:2106.01345"}) == "2106.01345"
    assert verifier.arxiv_id({"pages": "1706.03762"}) is None


def test_cite_contexts_extracts_sentences_and_ignores_comments():
    tex = "Transformers dominate NLP \\citep{vaswani, devlin}. % old claim \\cite{ghost}\n" \
          "Prior work used RNNs~\\cite[p.~3]{hochreiter}. Nothing cited here."
    contexts = verifier.cite_contexts(tex)
    assert set(contexts) == {"vaswani", "devlin", "hochreiter"}
    assert contexts["vaswani"] == ["Transformers dominate NLP \\citep{vaswani, devlin}."]


# ----------------------------------------------------------------- similarity

SOURCE = ("Deep neural networks have achieved remarkable success in image recognition tasks over the past decade. "
          "However, their decisions remain difficult to interpret for human experts.")


def test_similarity_flags_verbatim_close_and_quoted_differently():
    draft = ("Deep neural networks have achieved remarkable success in image recognition tasks in recent years. "
             "Their decisions remain difficult to interpret for experts, however. "
             "As the authors put it, \"their decisions remain difficult to interpret for human experts\" (p. 2). "
             "Our study instead examines rainfall patterns in coastal Gujarat.")
    result = sim.analyze(draft, {"src.txt": SOURCE})
    kinds = {item["sentence_number"]: item["kind"] for item in result["items"]}
    assert kinds == {1: "verbatim", 2: "close_paraphrase", 3: "quoted"}
    assert result["flagged"] == 2 and result["sentences"] == 4
    assert result["items"][0]["longest_copied_run"] == 11


def test_similarity_original_text_is_clean():
    result = sim.analyze("Rainfall in coastal Gujarat varies strongly with the monsoon onset date.", {"s": SOURCE})
    assert result["flagged"] == 0 and result["overall_trigram_overlap"] == 0.0


# ----------------------------------------------------------- csv_to_booktabs

ROWS = [["Method", "Acc_top1", "Error", "Params (M)", "Notes"],
        ["ResNet & co", "76.13", "23.87", "25.6", "baseline"],
        ["ViT-B", "81.07 ± 0.21", "18.93", "86.6", ""],
        ["Ours", "81.07 ± 0.10", "18.2", "22.1", "100% new"]]


def test_table_bolds_best_per_direction_and_escapes_text():
    tex = tables.build_table(ROWS, caption="Main results.", label="tab:main", lower_is_better={"Error"},
                             no_bold={"Params (M)"}, second=True, arrows=True, midrule_before="Ours")
    lines = tex.splitlines()
    assert r"\begin{tabular}{lcccl}" in tex
    assert r"Method & Acc\_top1 $\uparrow$ & Error $\downarrow$ & Params (M) & Notes \\" in tex
    assert r"ResNet \& co & \underline{76.13} & 23.87 & 25.6 & baseline \\" in tex
    assert r"ViT-B & \textbf{81.07 $\pm$ 0.21} & \underline{18.93} & 86.6 &  \\" in tex   # tie: both bold
    ours = r"    Ours & \textbf{81.07 $\pm$ 0.10} & \textbf{18.2} & 22.1 & 100\% new \\"
    assert lines[lines.index(ours) - 1] == r"    \midrule"
    assert r"\caption{Main results.}" in tex and r"\label{tab:main}" in tex
    assert tex.count(r"\toprule") == tex.count(r"\bottomrule") == 1


def test_table_rounding_makes_displayed_ties_bold():
    rows = [["M", "F1"], ["a", "0.912"], ["b", "0.914"], ["c", "0.85"]]
    tex = tables.build_table(rows, decimals=2)
    assert r"a & \textbf{0.91} \\" in tex and r"b & \textbf{0.91} \\" in tex and r"c & 0.85 \\" in tex


def test_table_rejects_unknown_columns_and_parses_cells():
    with pytest.raises(ValueError, match="not in the CSV header"):
        tables.build_table(ROWS, lower_is_better={"Nope"})
    assert tables.parse_cell("85.3 (0.4)") == {"value": 85.3, "raw": "85.3", "percent": False, "spread": "0.4", "paren": True}
    assert tables.parse_cell("12%")["percent"] is True and tables.parse_cell("n/a") is None


# ------------------------------------------------------------------ pubstyle

def test_figsize_uses_venue_widths():
    assert style.figsize("ieee", 1) == (3.5, 2.38)
    assert style.figsize("ieee", 2, height=2.0) == (7.16, 2.0)
    assert style.figsize("nature", 1)[0] == pytest.approx(3.504, abs=1e-3)
    with pytest.raises(ValueError):
        style.figsize("unknown")


def test_apply_embeds_truetype_fonts_and_demo_writes_files(tmp_path):
    style.apply("ieee")
    assert matplotlib.rcParams["pdf.fonttype"] == 42 and matplotlib.rcParams["font.size"] == 8
    written = style.demo("ieee", 1, str(tmp_path / "fig"))
    assert [w[-3:] for w in written] == ["pdf", "png"]
    assert (tmp_path / "fig.pdf").stat().st_size > 1000
