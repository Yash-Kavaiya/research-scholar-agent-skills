"""Copy shared/scholarly_api.py into every skill that uses it.

Skills must work when copied on their own, so each one carries its own copy as
scripts/_scholarly_api.py. Edit shared/scholarly_api.py, then run this script.
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared" / "scholarly_api.py"
COPY_NAME = "_scholarly_api.py"

# Skills whose scripts import _scholarly_api.
CONSUMERS = [
    "paper-search",
    "citation-graph-explorer",
    "topic-trend-analyzer",
    "novelty-checker",
    "dataset-finder",
    "citation-verifier",
    "bibtex-manager",
    "weekly-paper-digest",
]


def main() -> None:
    for name in CONSUMERS:
        scripts = ROOT / "skills" / name / "scripts"
        if not scripts.parent.is_dir():
            print(f"skip   {name} (skill not created yet)")
            continue
        scripts.mkdir(exist_ok=True)
        shutil.copyfile(SHARED, scripts / COPY_NAME)
        print(f"synced {name}")


if __name__ == "__main__":
    main()
