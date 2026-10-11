import json

import numpy as np
import pytest
from conftest import load_script

prisma = load_script("systematic-review-prisma", "prisma_flow")
power = load_script("sample-size-power-calculator", "power_calc")
tests = load_script("statistical-test-selector", "run_test")
datasets = load_script("dataset-finder", "find_datasets")
log = load_script("experiment-logger", "log_run")


# ---------------------------------------------------------------- prisma_flow

def test_dedupe_records_by_doi_and_title():
    records = [
        {"title": "Deep Learning for X", "doi": "10.1/A"},
        {"title": "Something else entirely", "doi": "https://doi.org/10.1/a"},   # same DOI
        {"title": "Deep learning for X.", "doi": ""},                             # same title
        {"title": "A different paper", "doi": ""},
    ]
    kept, removed = prisma.dedupe_records(records)
    assert removed == 2
    assert [r["title"] for r in kept] == ["Deep Learning for X", "A different paper"]


def test_read_ris_and_csv(tmp_path):
    ris = tmp_path / "pubmed.ris"
    ris.write_text("TY  - JOUR\nAU  - Smith, J\nAU  - Lee, K\nTI  - A trial\nPY  - 2021/03/01\nDO  - 10.1/x\nER  - \n",
                   encoding="utf-8")
    (record,) = prisma.read_records(ris)
    assert record == {"title": "A trial", "authors": "Smith, J; Lee, K", "year": "2021", "venue": "",
                      "doi": "10.1/x", "abstract": "", "source": "pubmed"}
    table = tmp_path / "scopus.csv"
    table.write_text("Article Title,Author,Publication Year,DOI\nA trial,Smith,2021,10.1/x\n", encoding="utf-8")
    (record,) = prisma.read_records(table)
    assert record["title"] == "A trial" and record["year"] == "2021" and record["source"] == "scopus"


def sheet():
    rows = [{"id": i, "title_abstract_decision": "exclude", "fulltext_decision": "", "exclusion_reason": ""}
            for i in range(1, 7)]
    rows += [
        {"id": 7, "title_abstract_decision": "include", "fulltext_decision": "include", "exclusion_reason": ""},
        {"id": 8, "title_abstract_decision": "Include", "fulltext_decision": "exclude", "exclusion_reason": "Wrong population"},
        {"id": 9, "title_abstract_decision": "include", "fulltext_decision": "exclude", "exclusion_reason": "Wrong population"},
        {"id": 10, "title_abstract_decision": "include", "fulltext_decision": "not retrieved", "exclusion_reason": ""},
    ]
    return rows


def test_tally_and_consistent_counts():
    tallied = prisma.tally_decisions(sheet())
    assert tallied == {"screened": 10, "excluded_screening": 6, "sought_retrieval": 4, "not_retrieved": 1,
                       "assessed_eligibility": 3, "excluded_fulltext": {"Wrong population": 2}, "included": 1}
    counts = {"identified": {"PubMed": 8, "Scopus": 5}, "duplicates_removed": 3, **tallied}
    assert prisma.check_counts(counts) == []
    counts["included"] = 2
    assert prisma.check_counts(counts) == ["included is 2 but assessed minus full-text exclusions gives 1"]


def test_tally_rejects_incomplete_sheets():
    rows = sheet()
    rows[0]["title_abstract_decision"] = ""
    with pytest.raises(ValueError, match="no title/abstract decision"):
        prisma.tally_decisions(rows)
    rows = sheet()
    rows[7]["exclusion_reason"] = ""
    with pytest.raises(ValueError, match="no exclusion_reason"):
        prisma.tally_decisions(rows)


def test_diagrams_contain_the_counts():
    counts = {"identified": {"PubMed": 8, "Scopus": 5}, "duplicates_removed": 3, **prisma.tally_decisions(sheet())}
    mermaid = prisma.to_mermaid(counts)
    assert mermaid.startswith("flowchart TD")
    assert "Records identified (n = 13): PubMed (n = 8); Scopus (n = 5)" in mermaid
    assert "Studies included in review (n = 1)" in mermaid
    tikz = prisma.to_tikz(counts)
    assert r"\begin{tikzpicture}" in tikz and "Wrong population (n = 2)" in tikz


# ----------------------------------------------------------------- power_calc
# Reference values: G*Power 3.1 for the t, F, and chi-square designs. The correlation design uses the
# Fisher z approximation, which gives 85 where G*Power's exact routine gives 84.

@pytest.mark.parametrize("design, kwargs, key, expected", [
    ("ttest-ind", {"effect": 0.5}, "n_group1", 64),
    ("ttest-ind", {"effect": 0.8}, "n_group1", 26),
    ("ttest-paired", {"effect": 0.5}, "n_pairs", 34),
    ("anova", {"effect": 0.25, "groups": 3}, "n_total", 159),
    ("chi2", {"effect": 0.3, "df": 1}, "n_total", 88),
    ("correlation", {"effect": 0.3}, "n_total", 85),
])
def test_required_sample_sizes_match_reference_values(design, kwargs, key, expected):
    result = power.compute(design, n=None, power=0.8, **kwargs)
    assert result[key] == expected
    assert result["achieved_power"] >= 0.8


def test_proportions_uses_cohens_h():
    h = power.cohen_h(0.5, 0.3)
    assert round(h, 4) == 0.4115
    assert power.compute("proportions", h, None, 0.8)["n_group1"] == 93


def test_power_and_detectable_effect_are_consistent():
    achieved = power.compute("ttest-ind", 0.5, 64, None)["achieved_power"]
    assert 0.80 <= achieved < 0.81
    effect = power.compute("ttest-ind", None, 64, 0.8)["effect_size"]
    assert abs(effect - 0.5) < 0.01


def test_one_sided_needs_fewer_and_dropout_inflates():
    assert power.compute("ttest-ind", 0.5, None, 0.8, two_sided=False)["n_group1"] == 51
    result = power.add_dropout(power.compute("ttest-ind", 0.5, None, 0.8), 0.2)
    assert result["n_total"] == 128 and result["n_total_to_recruit"] == 160
    assert "160 participants should be recruited" in power.sentence(result)


def test_missing_inputs_raise():
    with pytest.raises(ValueError):
        power.compute("ttest-ind", None, None, 0.8)


# ------------------------------------------------------------------- run_test

rng = np.random.default_rng(0)


def test_two_groups_normal_data_uses_welch_and_matches_scipy():
    a, b = rng.normal(10, 2, 40), rng.normal(12, 2, 40)
    result = tests.two_groups(a, b, ("a", "b"))
    assert result["test"] == "Welch's t test"
    assert result["p"] < 0.001 and "p < .001" in result["apa"]
    assert result["effect_size"]["value"] < -0.5


def test_two_groups_small_skewed_data_uses_mann_whitney():
    a, b = rng.exponential(1, 12) ** 3, rng.exponential(1, 12) ** 3 + 5
    result = tests.two_groups(a, b, ("a", "b"))
    assert result["test"] == "Mann-Whitney U test"
    assert -1 <= result["effect_size"]["value"] <= 1


def test_paired_design():
    before = rng.normal(50, 5, 25)
    after = before + rng.normal(2, 1, 25)
    result = tests.two_groups(after, before, ("after", "before"), paired=True)
    assert result["test"] == "Paired-samples t test" and result["df"] == 24
    assert result["apa"].startswith("t(24) = ")


def test_multi_groups_picks_by_assumptions():
    equal = {name: rng.normal(mean, 1, 30) for name, mean in (("a", 0), ("b", 0.2), ("c", 2))}
    result = tests.multi_groups(equal)
    assert result["test"] == "One-way ANOVA"
    assert len(result["posthoc"]["comparisons"]) == 3
    assert 0 < result["effect_size"]["value"] < 1
    unequal = {"a": rng.normal(0, 1, 40), "b": rng.normal(0, 8, 40), "c": rng.normal(3, 1, 40)}
    assert tests.multi_groups(unequal)["test"] == "Welch's ANOVA"
    skewed = {name: rng.exponential(1, 10) ** 4 + shift for name, shift in (("a", 0), ("b", 0), ("c", 50))}
    assert tests.multi_groups(skewed)["test"] == "Kruskal-Wallis test"


def test_welch_anova_with_two_groups_equals_welch_t_test():
    # With k = 2, Welch's F is the square of Welch's t, with the same error df and p-value.
    from scipy import stats
    a, b = np.array([1, 2, 3, 4, 5.0]), np.array([2, 4, 6, 8, 10.0, 13.0])
    f, df1, df2, p = tests.welch_anova([a, b])
    welch = stats.ttest_ind(a, b, equal_var=False)
    assert df1 == 1
    assert f == pytest.approx(welch.statistic ** 2)
    assert df2 == pytest.approx(welch.df)
    assert p == pytest.approx(welch.pvalue)


def test_welch_anova_equal_groups_gives_f_of_zero_and_p_of_one():
    f, _, _, p = tests.welch_anova([np.array([1, 2, 3.0]), np.array([0, 2, 4.0]), np.array([1.5, 2, 2.5])])
    assert f == pytest.approx(0) and p == pytest.approx(1)


def test_holm_adjustment():
    assert tests.holm([0.01, 0.04, 0.03]) == pytest.approx([0.03, 0.06, 0.06])


def test_correlation_and_formatting():
    x = rng.normal(0, 1, 50)
    result = tests.correlation(x, x * 0.8 + rng.normal(0, 0.5, 50))
    assert result["test"] == "Pearson correlation"
    assert result["apa"].startswith("r(48) = .")
    assert tests.fmt_p(0.0004) == "p < .001" and tests.fmt_p(0.0312) == "p = .031"


def test_categorical_switches_to_fisher_for_sparse_2x2():
    dense = tests.categorical(np.array([[30, 10], [15, 25]]), ["a", "b"], ["x", "y"])
    assert dense["test"] == "Chi-square test of independence" and "N = 80" in dense["apa"]
    sparse = tests.categorical(np.array([[1, 9], [8, 2]]), ["a", "b"], ["x", "y"])
    assert sparse["test"] == "Fisher's exact test"


# -------------------------------------------------------------- find_datasets

def test_parse_huggingface_reads_tags():
    (d,) = datasets.parse_huggingface([{"id": "stanfordnlp/imdb", "downloads": 100, "likes": 5, "gated": False,
                                        "lastModified": "2024-01-04T12:00:00.000Z",
                                        "tags": ["license:other", "task_categories:text-classification",
                                                 "size_categories:10K<n<100K", "language:en", "modality:text"]}])
    assert d["url"] == "https://huggingface.co/datasets/stanfordnlp/imdb"
    assert d["license"] == "other" and d["tasks"] == ["text-classification"]
    assert d["size"] == "10K<n<100K" and d["updated"] == "2024-01-04"


def test_parse_openml():
    (d,) = datasets.parse_openml({"data": {"dataset": [{"did": 31, "name": "credit-g", "version": 1, "status": "active",
                                 "quality": [{"name": "NumberOfInstances", "value": "1000.0"},
                                             {"name": "NumberOfFeatures", "value": "21.0"}]}]}})
    assert d["url"] == "https://www.openml.org/d/31" and d["size"] == "1000 rows x 21 features"


# -------------------------------------------------------------------- log_run

def test_log_roundtrip_best_diff_and_render(tmp_path):
    path = tmp_path / "exp" / "log.jsonl"
    first = log.append(path, {"type": "run", "name": "baseline", "status": "completed",
                              "config": {"lr": 0.1, "epochs": 90}, "metrics": {"top1": 76.1}, "tags": ["baseline"],
                              "git": {"commit": "abc1234", "dirty": True}})
    log.append(path, {"type": "decision", "text": "Keep cosine schedule"})
    third = log.append(path, {"type": "run", "name": "lr-low", "status": "completed",
                              "config": {"lr": 0.01, "epochs": 90}, "metrics": {"top1": 77.4}, "tags": []})
    entries = log.read_log(path)
    assert [e["id"] for e in entries] == [1, 2, 3]
    assert log.best_run(entries, "top1")["name"] == "lr-low"
    assert log.best_run(entries, "top1", "min")["name"] == "baseline"
    assert log.best_run(entries, "missing") is None
    assert log.diff_runs(first, third) == {"config": {"lr": [0.1, 0.01]}, "metrics": {"top1": [76.1, 77.4]}}
    notebook = log.render(entries)
    assert "| 1 | " in notebook and "abc1234*" in notebook and "Decision (#2)" in notebook
    assert json.loads(path.read_text(encoding="utf-8").splitlines()[1])["text"] == "Keep cosine schedule"


def test_parse_pairs_and_flatten():
    assert log.parse_pairs(["lr=0.1", "aug=true", "name=resnet", "layers=[2,2]"]) == {
        "lr": 0.1, "aug": True, "name": "resnet", "layers": [2, 2]}
    with pytest.raises(ValueError):
        log.parse_pairs(["novalue"])
    assert log.flatten({"opt": {"lr": 0.1, "sched": {"name": "cos"}}, "seed": 1}) == {
        "opt.lr": 0.1, "opt.sched.name": "cos", "seed": 1}
