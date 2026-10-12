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
