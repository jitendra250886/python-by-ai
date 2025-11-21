#!/usr/bin/env python3
"""Generate project templates for the Projects level (06-projects).

Creates standardized scaffolding for beginner, intermediate, advanced,
and domain-specific projects.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Project:
    slug: str
    title: str
    difficulty: str  # beginner, intermediate, advanced, domain
    path: str  # relative to 06-projects/
    summary: str


PROJECTS: list[Project] = [
    # Beginner projects
    Project(
        slug="calculator-gui",
        title="Calculator GUI",
        difficulty="beginner",
        path="beginner/calculator-gui",
        summary="Desktop calculator built with a simple GUI toolkit.",
    ),
    Project(
        slug="todo-list-app",
        title="To-Do List Application",
        difficulty="beginner",
        path="beginner/todo-list-app",
        summary="CLI or GUI-based to-do list for task management.",
    ),
    Project(
        slug="password-generator",
        title="Password Generator",
        difficulty="beginner",
        path="beginner/password-generator",
        summary="Generate secure passwords with configurable options.",
    ),
    Project(
        slug="quiz-game",
        title="Quiz Game",
        difficulty="beginner",
        path="beginner/quiz-game",
        summary="Multiple-choice quiz game with scoring.",
    ),
    Project(
        slug="file-organizer",
        title="File Organizer",
        difficulty="beginner",
        path="beginner/file-organizer",
        summary="Organize files into folders based on extension or rules.",
    ),
    # Intermediate projects
    Project(
        slug="weather-app",
        title="Weather App",
        difficulty="intermediate",
        path="intermediate/weather-app",
        summary="Fetch and display weather data from an external API.",
    ),
    Project(
        slug="web-scraper",
        title="Web Scraper",
        difficulty="intermediate",
        path="intermediate/web-scraper",
        summary="Scrape and store data from a target website.",
    ),
    Project(
        slug="rest-api",
        title="REST API Service",
        difficulty="intermediate",
        path="intermediate/rest-api",
        summary="Expose CRUD operations via a RESTful API.",
    ),
    Project(
        slug="data-analyzer",
        title="Data Analyzer",
        difficulty="intermediate",
        path="intermediate/data-analyzer",
        summary="Load, clean, and analyze CSV data with visualizations.",
    ),
    Project(
        slug="url-shortener",
        title="URL Shortener",
        difficulty="intermediate",
        path="intermediate/url-shortener",
        summary="Create short URLs that redirect to long URLs.",
    ),
    # Advanced projects
    Project(
        slug="ml-pipeline",
        title="Machine Learning Pipeline",
        difficulty="advanced",
        path="advanced/ml-pipeline",
        summary="End-to-end ML pipeline from preprocessing to deployment.",
    ),
    Project(
        slug="image-classifier",
        title="Image Classifier",
        difficulty="advanced",
        path="advanced/image-classifier",
        summary="Train and serve an image classification model.",
    ),
    Project(
        slug="automation-bot",
        title="Automation Bot",
        difficulty="advanced",
        path="advanced/automation-bot",
        summary="Bot that automates tasks (e.g., social media or chat).",
    ),
    Project(
        slug="chat-application",
        title="Chat Application",
        difficulty="advanced",
        path="advanced/chat-application",
        summary="Real-time chat app using websockets or similar.",
    ),
    Project(
        slug="stock-predictor",
        title="Stock Market Predictor",
        difficulty="advanced",
        path="advanced/stock-predictor",
        summary="Time-series forecasting for stock prices.",
    ),
    # Domain-specific
    Project(
        slug="patient-analyzer",
        title="Patient Data Analyzer",
        difficulty="domain",
        path="domain-specific/medical/patient-analyzer",
        summary="Analyze patient records and generate reports.",
    ),
    Project(
        slug="dicom-viewer",
        title="DICOM Viewer",
        difficulty="domain",
        path="domain-specific/medical/dicom-viewer",
        summary="View and inspect DICOM medical images.",
    ),
    Project(
        slug="temperature-monitor",
        title="IoT Temperature Monitor",
        difficulty="domain",
        path="domain-specific/iot/temperature-monitor",
        summary="Monitor temperature readings from IoT devices.",
    ),
    Project(
        slug="face-detection",
        title="Face Detection",
        difficulty="domain",
        path="domain-specific/computer-vision/face-detection",
        summary="Detect faces in images or video streams.",
    ),
    Project(
        slug="sales-forecasting",
        title="Sales Forecasting",
        difficulty="domain",
        path="domain-specific/data-science/sales-forecasting",
        summary="Predict sales using historical data.",
    ),
]


README_TEMPLATE = """# {title}

**Project slug:** `{slug}`  
**Difficulty:** {difficulty}

## Overview
{summary}

This folder provides a **template** for building the full project. It includes
starter code, a place for tests, and a basic requirements file.

## Structure
- `README.md` – this file
- `src/` – application source code (entrypoints, modules)
- `tests/` – test skeletons
- `solutions/` – space for reference/solution code
- `requirements.txt` – project dependencies

## Getting Started
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open `src/main.py` and follow the TODOs.
4. Add tests under `tests/` and run them regularly.

## Next Steps
- Replace TODOs with real code.
- Connect this project with course notebooks and applications.
- Document design decisions and trade-offs.
"""


STARTER_CODE = (
    '"""Entry point for the {title} project.\n\n'
    'Follow the TODO comments to implement the full project.\n'
    '"""\n'
)


STARTER_MAIN = """if __name__ == "__main__":
    # TODO: Implement command-line interface or app bootstrap here
    print("{title} template - start coding here!")
"""


TEST_SKELETON = """import pytest


@pytest.mark.skip("Add real tests for {title}")
def test_placeholder():
    assert True
"""


def create_project(project_root: Path, project: Project) -> None:
    base = project_root / project.path
    src = base / "src"
    tests = base / "tests"
    solutions = base / "solutions"

    for d in (src, tests, solutions):
        d.mkdir(parents=True, exist_ok=True)

    # README
    (base / "README.md").write_text(
        README_TEMPLATE.format(
            title=project.title,
            slug=project.slug,
            difficulty=project.difficulty,
            summary=project.summary,
        ),
        encoding="utf-8",
    )

    # Starter code
    (src / "__init__.py").write_text("", encoding="utf-8")
    (src / "main.py").write_text(
        STARTER_CODE.format(title=project.title) + "\n" + STARTER_MAIN.format(title=project.title),
        encoding="utf-8",
    )

    # Test skeleton
    (tests / "test_main.py").write_text(
        TEST_SKELETON.format(title=project.title),
        encoding="utf-8",
    )

    # Requirements
    (base / "requirements.txt").write_text("# TODO: Add project-specific dependencies\n", encoding="utf-8")


def main() -> None:
    script_dir = Path(__file__).parent
    project_root = script_dir.parent / "06-projects"
    project_root.mkdir(exist_ok=True)

    print(f"Generating project templates in: {project_root}")

    for project in PROJECTS:
        create_project(project_root, project)
        print(f"  ✓ Created template: {project.path}")

    print("\n✅ Project templates generated successfully.")


if __name__ == "__main__":
    main()
