from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "shared"))
sys.path.insert(0, str(ROOT / "tools"))


def load_script(skill: str, script: str):
    """Import skills/<skill>/scripts/<script>.py as a module, the way it runs from the CLI."""
    scripts_dir = ROOT / "skills" / skill / "scripts"
    path = scripts_dir / f"{script}.py"
    sys.path.insert(0, str(scripts_dir))
    try:
        spec = importlib.util.spec_from_file_location(f"{skill.replace('-', '_')}__{script}", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    finally:
        sys.path.remove(str(scripts_dir))
    return module
