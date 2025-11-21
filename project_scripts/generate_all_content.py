#!/usr/bin/env python3
"""Master generator for Python Master Course content.

This script orchestrates all individual generators:
- Beginner notebooks
- Intermediate notebooks
- Advanced notebooks
- Libraries notebooks
- Applications templates
- Project templates
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).parent.parent
SCRIPTS = ROOT / "project_scripts"


def run(cmd: list[str]) -> None:
    print("\n$", " ".join(cmd))
    subprocess.run(cmd, check=True)


def generate_section(section: str) -> None:
    section = section.lower()
    if section == "beginner":
        run(["python", str(SCRIPTS / "generate_beginner_notebooks.py")])
    elif section == "intermediate":
        run(["python", str(SCRIPTS / "generate_intermediate_notebooks.py")])
    elif section == "advanced":
        run(["python", str(SCRIPTS / "generate_advanced_notebooks.py")])
    elif section == "libraries":
        run(["python", str(SCRIPTS / "generate_libraries_notebooks.py")])
    elif section == "applications":
        run(["python", str(SCRIPTS / "generate_applications_content.py")])
    elif section == "projects":
        run(["python", str(SCRIPTS / "generate_project_templates.py")])
    elif section == "all":
        for name in [
            "beginner",
            "intermediate",
            "advanced",
            "libraries",
            "applications",
            "projects",
        ]:
            generate_section(name)
    else:
        raise SystemExit(f"Unknown section: {section}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate all course content.")
    parser.add_argument(
        "--section",
        "-s",
        default="all",
        help="Which section to generate (beginner, intermediate, advanced, libraries, applications, projects, all)",
    )
    args = parser.parse_args()

    generate_section(args.section)
    print("\n✅ Content generation completed.")


if __name__ == "__main__":
    main()
