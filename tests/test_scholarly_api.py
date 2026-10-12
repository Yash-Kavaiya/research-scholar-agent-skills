import scholarly_api as api

ARXIV_XML = b"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/1706.03762v7</id>
    <published>2017-06-12T17:57:34Z</published>
    <title>Attention Is All
      You Need</title>
    <summary>  The dominant sequence transduction models are based on RNNs.  </summary>
    <author><name>Ashish Vaswani</name></author>
    <author><name>Noam Shazeer</name></author>
    <arxiv:doi>10.48550/arXiv.1706.03762</arxiv:doi>
  </entry>
</feed>"""

S2_JSON = {"data": [{
    "paperId": "abc123", "title": "Attention is All you Need", "year": 2017, "venue": "NIPS",
    "authors": [{"name": "Ashish Vaswani"}], "externalIds": {"DOI": "10.5555/3295222.3295349"},
    "abstract": None, "citationCount": 100000, "url": "https://www.semanticscholar.org/paper/abc123",
}]}

OPENALEX_JSON = {"results": [{
    "id": "https://openalex.org/W2963403868", "title": "Attention Is All You Need",
    "publication_year": 2017, "publication_date": "2017-06-12",
    "doi": "https://doi.org/10.48550/ARXIV.1706.03762", "cited_by_count": 90000,
    "authorships": [{"author": {"display_name": "Ashish Vaswani"}}],
    "primary_location": {"landing_page_url": "https://arxiv.org/abs/1706.03762",
                         "source": {"display_name": "arXiv"}},
    "abstract_inverted_index": {"models": [2], "The": [0], "dominant": [1]},
    "referenced_works": ["https://openalex.org/W1"],
}]}

PUBMED_JSON = {"result": {"uids": ["123"], "123": {
    "title": "A trial of something.", "pubdate": "2021 Mar", "fulljournalname": "The Lancet",
    "authors": [{"name": "Smith J"}], "articleids": [{"idtype": "pubmed", "value": "123"},
                                                      {"idtype": "doi", "value": "10.1016/X"}],
}}}

CROSSREF_JSON = {"message": {"items": [{
    "DOI": "10.1038/NATURE14539", "title": ["Deep learning"], "container-title": ["Nature"],
    "author": [{"given": "Yann", "family": "LeCun"}, {"name": "Consortium"}],
    "issued": {"date-parts": [[2015, 5, 27]]}, "is-referenced-by-count": 50000,
    "URL": "https://doi.org/10.1038/nature14539", "type": "journal-article",
    "volume": "521", "page": "436-444", "abstract": "<jats:p>Deep learning allows</jats:p>",
}]}}


def test_normalize_doi_strips_prefixes_and_case():
    assert api.normalize_doi("https://doi.org/10.1038/NATURE14539.") == "10.1038/nature14539"
    assert api.normalize_doi("doi: 10.1/ABC") == "10.1/abc"
    assert api.normalize_doi(None) == ""


def test_normalize_title_ignores_case_accents_braces_and_punctuation():
    assert api.normalize_title("{BERT}: Pre-training of Déep Models!") == "bert pre training of deep models"


def test_title_similarity():
    assert api.title_similarity("Attention Is All You Need", "attention is all you need.") == 1.0
    assert api.title_similarity("Attention Is All You Need", "Deep Residual Learning") == 0.0


def test_parse_arxiv():
    (paper,) = api.parse_arxiv(ARXIV_XML)
    assert paper["title"] == "Attention Is All You Need"
    assert paper["authors"] == ["Ashish Vaswani", "Noam Shazeer"]
    assert paper["year"] == 2017
    assert paper["id"] == "1706.03762"
    assert paper["doi"] == "10.48550/arxiv.1706.03762"
    assert paper["abstract"].startswith("The dominant")
    assert paper["source"] == "arxiv"


def test_parse_s2_handles_null_abstract():
    (paper,) = api.parse_s2(S2_JSON)
    assert paper["abstract"] == ""
    assert paper["citations"] == 100000
    assert paper["doi"] == "10.5555/3295222.3295349"


def test_parse_openalex_rebuilds_abstract_and_ids():
    (paper,) = api.parse_openalex(OPENALEX_JSON)
    assert paper["abstract"] == "The dominant models"
    assert paper["id"] == "W2963403868"
    assert paper["venue"] == "arXiv"
    assert paper["referenced_works"] == ["W1"]
    assert paper["doi"] == "10.48550/arxiv.1706.03762"


def test_parse_pubmed_summary():
    (paper,) = api.parse_pubmed_summary(PUBMED_JSON)
    assert paper["title"] == "A trial of something"
    assert paper["year"] == 2021
    assert paper["doi"] == "10.1016/x"
    assert paper["url"] == "https://pubmed.ncbi.nlm.nih.gov/123/"


def test_parse_crossref():
    (paper,) = api.parse_crossref(CROSSREF_JSON)
    assert paper["authors"] == ["Yann LeCun", "Consortium"]
    assert paper["year"] == 2015
    assert paper["venue"] == "Nature"
    assert paper["pages"] == "436-444"
    assert paper["abstract"] == "Deep learning allows"


def test_dedupe_merges_by_doi_and_by_title():
    arxiv = api.parse_arxiv(ARXIV_XML)[0]
    openalex = api.parse_openalex(OPENALEX_JSON)[0]   # same DOI as arXiv
    s2 = api.parse_s2(S2_JSON)[0]                     # different DOI, same title
    other = api.parse_crossref(CROSSREF_JSON)[0]
    merged = api.dedupe([arxiv, openalex, s2, other])
    assert len(merged) == 2
    first = merged[0]
    assert first["sources"] == ["arxiv", "openalex", "semantic_scholar"]
    assert first["citations"] == 100000          # highest count wins
    assert first["abstract"].startswith("The dominant sequence")  # first non-empty wins


def test_filter_years():
    papers = [api.make_paper(title="a", year=2019), api.make_paper(title="b", year=2023),
              api.make_paper(title="c", year=None)]
    assert [p["title"] for p in api.filter_years(papers, year_from=2020)] == ["b"]
    assert len(api.filter_years(papers)) == 3


def test_to_markdown_contains_core_fields():
    text = api.to_markdown(api.dedupe(api.parse_crossref(CROSSREF_JSON)), abstract_chars=4)
    assert "**Deep learning** (2015)" in text
    assert "50000 citations" in text
    assert "> Deep…" in text


def test_search_all_reports_failed_source(monkeypatch):
    def boom(query, limit=10):
        raise api.ApiError("HTTP 429")
    monkeypatch.setitem(api._SEARCHERS, "arxiv", boom)
    monkeypatch.setitem(api._SEARCHERS, "crossref", lambda query, limit=10: api.parse_crossref(CROSSREF_JSON))
    papers, errors = api.search_all("x", sources=("arxiv", "crossref"), pause=0)
    assert len(papers) == 1
    assert errors == {"arxiv": "HTTP 429"}
