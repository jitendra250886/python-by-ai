#!/usr/bin/env python3
"""Validate basic Python Master Course structure.

Checks that expected key directories and index files exist and that
notebook counts roughly match the curriculum.

This is intentionally lightweight and can be extended later.
"""

from __future__ import annotations

from pathlib import Path
import re
from typing import Iterable


ROOT = Path(__file__).parent.parent


def check_path(path: Path, kind: str) -> bool:
    if kind == "dir":
        ok = path.is_dir()
    else:
        ok = path.is_file()
    status = "OK" if ok else "MISSING"
    print(f"[{status:7}] {path.relative_to(ROOT)}")
    return ok


def parse_expected_notebooks(index_path: Path) -> list[str]:
    """Parse INDEX.md and extract expected notebook filenames.

    Looks for patterns like ``01_lesson_name.ipynb`` in the text.
    """
    text = index_path.read_text(encoding="utf-8")
    # Require two leading digits to avoid accidental matches.
    pattern = re.compile(r"\b(\d{2}_[a-zA-Z0-9_]+\.ipynb)\b")
    return sorted(set(pattern.findall(text)))


def compare_index_with_files(label: str, dir_path: Path, index_path: Path) -> bool:
    """Compare expected notebooks from INDEX.md with actual files on disk."""
    expected = set(parse_expected_notebooks(index_path))
    actual = {p.name for p in dir_path.glob("*.ipynb")} if dir_path.is_dir() else set()

    missing = sorted(expected - actual)
    extra = sorted(actual - expected)

    print(f"\n{label} – INDEX vs filesystem:")
    print(f"  Expected from INDEX.md: {len(expected)}")
    print(f"  Actual .ipynb files  : {len(actual)}")

    ok = True
    if missing:
        ok = False
        print("  Missing notebooks (listed in INDEX.md but not found on disk):")
        for name in missing:
            print(f"    - {name}")
    if extra:
        ok = False
        print("  Extra notebooks (present on disk but not listed in INDEX.md):")
        for name in extra:
            print(f"    - {name}")
    if ok:
        print("  ✓ INDEX.md and directory are in sync.")
    return ok


def main() -> None:
    print("Validating Python Master Course structure...\n")

    required_dirs = [
        ROOT / "01-beginner",
        ROOT / "02-intermediate",
        ROOT / "03-advanced",
        ROOT / "04-libraries",
        ROOT / "05-applications",
        ROOT / "06-projects",
    ]

    required_files = [
        ROOT / "01-beginner" / "INDEX.md",
        ROOT / "02-intermediate" / "INDEX.md",
        ROOT / "03-advanced" / "INDEX.md",
        ROOT / "04-libraries" / "INDEX.md",
        ROOT / "05-applications" / "INDEX.md",
        ROOT / "06-projects" / "INDEX.md",
    ]

    ok = True
    print("Required directories:")
    for d in required_dirs:
        ok &= check_path(d, "dir")

    print("\nRequired index files:")
    for f in required_files:
        ok &= check_path(f, "file")

    # Cross-check INDEX.md filenames with actual notebooks
    for label, dirname in [
        ("Beginner", "01-beginner"),
        ("Intermediate", "02-intermediate"),
        ("Advanced", "03-advanced"),
        ("Libraries", "04-libraries"),
    ]:
        dir_path = ROOT / dirname
        index_path = dir_path / "INDEX.md"
        if dir_path.is_dir() and index_path.is_file():
            ok &= compare_index_with_files(label, dir_path, index_path)
        else:
            ok = False
            print(f"\n{label} – cannot compare, missing dir or INDEX.md")

    print("\nValidation:")
    if ok:
        print("✅ Structure looks complete.")
        raise SystemExit(0)
    else:
        print("❌ Structure has missing items; see messages above.")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
