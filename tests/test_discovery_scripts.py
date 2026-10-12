import scholarly_api as api
from conftest import load_script

graph = load_script("citation-graph-explorer", "citation_graph")
trend = load_script("topic-trend-analyzer", "trend_counts")
closest = load_script("novelty-checker", "closest_work")
search = load_script("paper-search", "search_papers")


def paper(pid, title, citations=0, **extra):
    return api.make_paper(id=pid, title=title, citations=citations, source="openalex", **extra)


def test_rank_seminal_prefers_references_shared_by_more_seeds():
    shared = paper("W1", "Shared foundation", citations=10)
    famous = paper("W2", "Famous but cited by one seed", citations=99999)
    ranked = graph.rank_seminal({"S1": [shared, famous], "S2": [shared]})
    assert [p["id"] for p in ranked] == ["W1", "W2"]
    assert ranked[0]["cited_by_seeds"] == ["S1", "S2"]


def test_top_cited_orders_by_citations_and_handles_none():
    papers = [paper("a", "a", None), paper("b", "b", 5), paper("c", "c", 50)]
    assert [p["id"] for p in graph.top_cited(papers, 2)] == ["c", "b"]


def test_group_counts_and_yearly_series_fill_missing_years():
    counts = trend.group_counts({"group_by": [{"key": "2020", "key_display_name": "2020", "count": 10},
                                              {"key": "2022", "key_display_name": "2022", "count": 30}]})
    series = trend.yearly_series(counts, {"2020": 1000, "2021": 1000, "2022": 2000}, 2020, 2022)
    assert [r["count"] for r in series] == [10, 0, 30]
    assert [r["share_per_10k"] for r in series] == [100.0, 0.0, 150.0]


def test_cagr():
    assert round(trend.cagr(100, 400, 2), 6) == 1.0
    assert trend.cagr(0, 50, 3) is None


def test_growth_table_lists_new_groups_first_then_by_ratio_and_drops_tiny_ones():
    rows = trend.growth_table({"A": 40, "B": 30, "New": 12, "Tiny": 2}, {"A": 10, "B": 20, "Tiny": 1})
    assert [r["name"] for r in rows] == ["New", "A", "B"]
    assert rows[0]["ratio"] is None and rows[1]["ratio"] == 4.0


def test_rank_closest_scores_overlap_and_query_hits():
    idea = "contrastive pretraining on ECG signals for arrhythmia detection"
    close = paper("1", "Contrastive pretraining for ECG arrhythmia detection", doi="10.1/a")
    far = paper("2", "A survey of protein folding", doi="10.1/b")
    ranked = closest.rank_closest(idea, {"q1": [close, far], "q2": [close]})
    assert ranked[0]["id"] == "1"
    assert ranked[0]["found_by_queries"] == ["q1", "q2"]
    assert ranked[0]["overlap"] > 0.5
    assert ranked[1]["overlap"] == 0.0 and ranked[1]["matched_terms"] == []


def test_content_terms_drops_stopwords_and_short_words():
    assert closest.content_terms("We propose a novel GNN for the ECG") == ["gnn", "ecg"]


def test_sort_papers():
    papers = [dict(paper("a", "a", 1, year=2020), sources=["x"]),
              dict(paper("b", "b", 9, year=2018), sources=["x", "y"])]
    assert [p["id"] for p in search.sort_papers(papers, "relevance")] == ["b", "a"]
    assert [p["id"] for p in search.sort_papers(papers, "year")] == ["a", "b"]
    assert [p["id"] for p in search.sort_papers(papers, "citations")] == ["b", "a"]


def test_growth_table_reports_floor_when_earlier_window_is_truncated():
    earlier = {f"g{i}": 50 + i for i in range(trend.GROUP_LIMIT)}
    rows = trend.growth_table({"g0": 100, "Missing": 80}, earlier)
    missing = next(r for r in rows if r["name"] == "Missing")
    assert missing["earlier_below"] == 50 and missing["ratio"] is None
    assert next(r for r in rows if r["name"] == "g0")["earlier_below"] is None


def test_topic_params_defaults_to_phrase_in_title_and_abstract():
    assert trend.topic_params("diffusion models", False, "publication_year:2020-2022") == {
        "filter": 'title_and_abstract.search:"diffusion models",publication_year:2020-2022'}
    assert trend.topic_params("diffusion models", True, "y") == {"search": "diffusion models", "filter": "y"}
