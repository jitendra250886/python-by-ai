#!/usr/bin/env python3
"""Generate example application notebooks for the Applications level (05-applications).

This script creates a small set of template notebooks and README files that
show how to build end-to-end Python applications in different categories.

The goal is to provide a consistent structure that can later be expanded
into full applications.
"""

from pathlib import Path
import json


def create_notebook_structure(title: str, cells: list[dict]) -> dict:
    """Create a minimal Jupyter notebook structure."""
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "pygments_lexer": "ipython3",
                "nbconvert_exporter": "python",
                "version": "3.8.0",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def markdown_cell(source: str | list[str]) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": source if isinstance(source, list) else [source],
    }


def code_cell(source: str | list[str]) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source if isinstance(source, list) else [source],
    }


APPLICATIONS = [
    {
        "slug": "web",
        "title": "Web Application: Simple Dashboard",
        "description": "Build a small web dashboard using a Python web framework.",
    },
    {
        "slug": "data-analysis",
        "title": "Data Analysis Application: Sales Report",
        "description": "Create a data pipeline that loads, cleans, and visualizes data.",
    },
    {
        "slug": "ml",
        "title": "Machine Learning Application: Model Service",
        "description": "Train a model and expose it via a simple API.",
    },
    {
        "slug": "automation",
        "title": "Automation Script: File Organizer Bot",
        "description": "Automate repetitive file operations and scheduling.",
    },
    {
        "slug": "desktop",
        "title": "Desktop Application: Utility Tool",
        "description": "Create a small GUI application for everyday tasks.",
    },
]


def build_notebook(app: dict) -> dict:
    title = app["title"]
    description = app["description"]
    slug = app["slug"]

    cells: list[dict] = [
        markdown_cell(
            [
                f"# {title}\n",
                "\n",
                f"Category: `{slug}` applications\n",
                "\n",
                "## Overview\n",
                f"{description}\n",
                "\n",
                "This notebook is a **template**. Replace TODO sections with a full implementation.\n",
                "\n",
                "---\n",
            ]
        ),
        markdown_cell(
            [
                "## 1. Requirements & Architecture\n",
                "\n",
                "- TODO: Describe the problem this application solves.\n",
                "- TODO: List user stories.\n",
                "- TODO: Sketch a simple architecture diagram.\n",
            ]
        ),
        markdown_cell(
            [
                "## 2. Environment Setup\n",
                "\n",
                "- TODO: List required libraries.\n",
                "- TODO: Add installation commands (pip/conda).\n",
            ]
        ),
        code_cell(
            [
                "# Example: import libraries here\n",
                "# import pandas as pd\n",
                "# import requests\n",
                "print(\"Environment ready!\")\n",
            ]
        ),
        markdown_cell(
            [
                "## 3. Core Implementation\n",
                "\n",
                "Break your application into clear steps (data loading, processing, UI, etc.).\n",
                "\n",
                "### Step 1\n",
                "TODO: Describe and implement step 1.\n",
            ]
        ),
        code_cell("# TODO: Implement step 1 here\n"),
        markdown_cell(
            [
                "### Step 2\n",
                "TODO: Describe and implement step 2.\n",
            ]
        ),
        code_cell("# TODO: Implement step 2 here\n"),
        markdown_cell(
            [
                "### Step 3\n",
                "TODO: Describe and implement step 3.\n",
            ]
        ),
        code_cell("# TODO: Implement step 3 here\n"),
        markdown_cell(
            [
                "## 4. Testing & Validation\n",
                "\n",
                "- TODO: Describe how to test the application.\n",
                "- TODO: Add manual test cases or simple assertions.\n",
            ]
        ),
        code_cell("# TODO: Add simple tests or validation checks here\n"),
        markdown_cell(
            [
                "## 5. Deployment Notes\n",
                "\n",
                "- TODO: Describe how this app would be deployed (local, server, cloud).\n",
                "- TODO: Mention configuration, environment variables, or services needed.\n",
            ]
        ),
        markdown_cell(
            [
                "## 6. Next Steps\n",
                "\n",
                "- TODO: List possible improvements and extensions.\n",
                "- TODO: Connect this application to bigger projects in `06-projects/`.\n",
            ]
        ),
    ]

    return create_notebook_structure(title, cells)


def write_readme(app_dir: Path, app: dict) -> None:
    contents = f"""# {app['title']}

Category: `{app['slug']}` applications

## Overview
{app['description']}

This folder contains a **template application** for the Applications level of the
Python Master Course. The main notebook walks through requirements, architecture,
implementation steps, testing, and deployment notes.

## Files
- `main.ipynb` – primary walkthrough notebook

## How to Use
1. Open `main.ipynb` in Jupyter Lab/Notebook.
2. Follow the sections in order, replacing TODOs with real implementation.
3. Extend the template into a full application and integrate it with content from
   `04-libraries/` and `06-projects/` if desired.
"""
    app_dir.mkdir(parents=True, exist_ok=True)
    (app_dir / "README.md").write_text(contents, encoding="utf-8")


def main() -> None:
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    apps_root = project_root / "05-applications"
    apps_root.mkdir(exist_ok=True)

    print(f"Generating application templates in: {apps_root}")

    for app in APPLICATIONS:
        app_dir = apps_root / app["slug"]
        app_dir.mkdir(exist_ok=True)

        # Notebook
        notebook = build_notebook(app)
        notebook_path = app_dir / "main.ipynb"
        with notebook_path.open("w", encoding="utf-8") as f:
            json.dump(notebook, f, indent=2, ensure_ascii=False)

        # README
        write_readme(app_dir, app)

        print(f"  ✓ Created application template: {app['slug']} -> {notebook_path}")

    print("\n✅ Applications templates generated successfully.")


if __name__ == "__main__":
    main()
