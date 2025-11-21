#!/usr/bin/env python3
"""Wrapper script to re-generate specific course sections.

This is a thin convenience layer around generate_all_content.py so that
maintainers can quickly refresh parts of the course.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess


ROOT = Path(__file__).parent.parent


def main() -> None:
    parser = argparse.ArgumentParser(description="Update course content for a given section.")
    parser.add_argument(
        "section",
        help="Section to update (beginner, intermediate, advanced, libraries, applications, projects, all)",
    )
    args = parser.parse_args()

    script = ROOT / "project_scripts" / "generate_all_content.py"
    cmd = ["python", str(script), "--section", args.section]
    print("$", " ".join(cmd))
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
