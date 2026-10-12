import json
import re

import validate_skills
from conftest import ROOT

SCRIPTED = {
    "paper-search", "citation-graph-explorer", "topic-trend-analyzer", "novelty-checker", "dataset-finder",
    "systematic-review-prisma", "sample-size-power-calculator", "statistical-test-selector", "experiment-logger",
    "publication-figure-maker", "latex-table-generator", "citation-verifier", "bibtex-manager",
    "plagiarism-and-paraphrase-checker", "camera-ready-checker", "weekly-paper-digest",
}


def test_all_skills_validate():
    assert validate_skills.validate() == []
    assert len(validate_skills.load_catalog()) == 59


def test_frontmatter_is_valid_yaml_with_required_fields():
    import yaml

    for path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        front = path.read_text(encoding="utf-8")[4:].split("\n---\n", 1)[0]
        meta = yaml.safe_load(front)                       # raises on invalid YAML, e.g. an unquoted ': '
        assert meta["name"] == path.parent.name
        assert isinstance(meta["description"], str) and len(meta["description"]) <= 200
        assert meta["version"] == "1.0.0"
        assert 1 <= len(meta["metadata"]["tags"]) <= 5 and "@" in meta["metadata"]["author"]
        if (path.parent / "scripts").is_dir():
            assert meta.get("allowed-tools") and meta.get("compatibility"), path.parent.name


def test_eval_datasets_match_the_examples_sections():
    import build_eval_datasets

    for skill_dir in sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir()):
        expected = build_eval_datasets.build(skill_dir)
        actual = json.loads((skill_dir / "evals" / "evals.json").read_text(encoding="utf-8"))
        assert actual == expected, f"{skill_dir.name}: run python tools/build_eval_datasets.py"
        assert [case["expected_skill"] for case in actual["evals"]][:2] == [skill_dir.name] * 2
        assert actual["evals"][2]["expected_skill"] != skill_dir.name


def test_no_bytecode_is_left_inside_skills():
    assert list((ROOT / "skills").rglob("__pycache__")) == []


def test_scripted_skills_are_exactly_the_planned_set():
    with_scripts = {p.parent.name for p in (ROOT / "skills").glob("*/scripts") if any(p.glob("[!_]*.py"))}
    assert with_scripts == SCRIPTED


def test_orchestrator_routes_to_every_other_skill():
    text = (ROOT / "skills" / "research-scholar-orchestrator" / "SKILL.md").read_text(encoding="utf-8")
    mentioned = set(re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", text))
    others = set(validate_skills.load_catalog()) - {"research-scholar-orchestrator"}
    assert others - mentioned == set()


def test_plugin_manifests_are_consistent():
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    assert [p["name"] for p in market["plugins"]] == [plugin["name"]]


def test_readme_lists_every_skill():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    missing = [name for name in validate_skills.load_catalog() if f"`{name}`" not in readme]
    assert missing == []
