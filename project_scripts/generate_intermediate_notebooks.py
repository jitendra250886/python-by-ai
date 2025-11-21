#!/usr/bin/env python3
"""
Generate Jupyter notebook files for the intermediate Python course.
This script creates 30 structured notebooks with templates for all lessons.
"""

import json
from pathlib import Path


def create_notebook_structure(title, cells):
    """Create a Jupyter notebook structure."""
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }


def markdown_cell(content):
    """Create a markdown cell."""
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": content if isinstance(content, list) else [content]
    }


def code_cell(code, outputs=None):
    """Create a code cell."""
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": outputs or [],
        "source": code if isinstance(code, list) else [code]
    }


# Lesson definitions for intermediate course
LESSONS = {
    "01_classes_deep_dive.ipynb": ("Lesson 1: Classes Deep Dive", "Module 1: Advanced OOP"),
    "02_inheritance_polymorphism.ipynb": ("Lesson 2: Inheritance & Polymorphism", "Module 1: Advanced OOP"),
    "03_encapsulation_abstraction.ipynb": ("Lesson 3: Encapsulation & Abstraction", "Module 1: Advanced OOP"),
    "04_magic_methods.ipynb": ("Lesson 4: Magic Methods (Dunder Methods)", "Module 1: Advanced OOP"),
    
    "05_list_comprehensions.ipynb": ("Lesson 5: List Comprehensions", "Module 2: Advanced Data Structures"),
    "06_dict_set_comprehensions.ipynb": ("Lesson 6: Dict & Set Comprehensions", "Module 2: Advanced Data Structures"),
    "07_generators_iterators.ipynb": ("Lesson 7: Generators & Iterators", "Module 2: Advanced Data Structures"),
    "08_collections_module.ipynb": ("Lesson 8: Collections Module", "Module 2: Advanced Data Structures"),
    
    "09_lambda_functions.ipynb": ("Lesson 9: Lambda Functions & Functional Tools", "Module 3: Functional Programming"),
    "10_decorators_basics.ipynb": ("Lesson 10: Decorators Basics", "Module 3: Functional Programming"),
    "11_advanced_decorators.ipynb": ("Lesson 11: Advanced Decorators", "Module 3: Functional Programming"),
    
    "12_advanced_file_handling.ipynb": ("Lesson 12: Advanced File Handling", "Module 4: File Operations"),
    "13_json_handling.ipynb": ("Lesson 13: JSON Handling", "Module 4: File Operations"),
    "14_csv_excel_operations.ipynb": ("Lesson 14: CSV & Excel Operations", "Module 4: File Operations"),
    "15_pickle_serialization.ipynb": ("Lesson 15: Pickle Serialization", "Module 4: File Operations"),
    
    "16_advanced_exceptions.ipynb": ("Lesson 16: Advanced Exception Handling", "Module 5: Error Handling"),
    "17_logging_debugging.ipynb": ("Lesson 17: Logging & Debugging", "Module 5: Error Handling"),
    "18_testing_basics.ipynb": ("Lesson 18: Testing Basics (unittest, pytest)", "Module 5: Error Handling"),
    
    "19_http_requests.ipynb": ("Lesson 19: HTTP Requests", "Module 6: APIs & Web"),
    "20_web_scraping.ipynb": ("Lesson 20: Web Scraping", "Module 6: APIs & Web"),
    "21_rest_api_basics.ipynb": ("Lesson 21: REST API Basics", "Module 6: APIs & Web"),
    
    "22_regex_fundamentals.ipynb": ("Lesson 22: Regular Expressions Fundamentals", "Module 7: Regular Expressions"),
    "23_regex_advanced.ipynb": ("Lesson 23: Regular Expressions Advanced", "Module 7: Regular Expressions"),
    
    "24_virtual_environments.ipynb": ("Lesson 24: Virtual Environments", "Module 8: Environment & Packages"),
    "25_package_management.ipynb": ("Lesson 25: Package Management", "Module 8: Environment & Packages"),
    
    "26_context_managers.ipynb": ("Lesson 26: Context Managers", "Module 9: Advanced Topics"),
    "27_metaclasses_intro.ipynb": ("Lesson 27: Metaclasses Introduction", "Module 9: Advanced Topics"),
    "28_type_hints.ipynb": ("Lesson 28: Type Hints & Annotations", "Module 9: Advanced Topics"),
    
    "29_intermediate_exercises.ipynb": ("Lesson 29: Intermediate Exercises", "Module 10: Practice & Projects"),
    "30_intermediate_projects.ipynb": ("Lesson 30: Intermediate Projects", "Module 10: Practice & Projects"),
}


def create_lesson_template(title, module, lesson_topics):
    """Create a template for a lesson."""
    return {
        "title": title,
        "cells": [
            markdown_cell([
                f"# {title}\n",
                f"**{module}**\n",
                "\n",
                "## Overview\n",
                f"In this lesson, you'll learn about {lesson_topics}.\n",
                "\n",
                "## Topics Covered\n",
                "- Core concepts and theory\n",
                "- Practical examples\n",
                "- Best practices\n",
                "- Common use cases\n",
                "- Hands-on exercises\n",
                "\n",
                "---"
            ]),
            markdown_cell([
                "## Introduction\n",
                "\n",
                "**TODO:** Add detailed introduction and explanation of concepts."
            ]),
            code_cell([
                "# Example code placeholder\n",
                "# TODO: Add practical examples\n",
                "\n",
                "print(\"Lesson content coming soon!\")"
            ]),
            markdown_cell([
                "---\n",
                "## Key Concepts\n",
                "\n",
                "**TODO:** Explain key concepts with examples."
            ]),
            code_cell([
                "# Additional code examples\n",
                "pass"
            ]),
            markdown_cell([
                "---\n",
                "## Practical Examples\n",
                "\n",
                "**TODO:** Add real-world examples and use cases."
            ]),
            code_cell([
                "# Real-world example placeholder\n",
                "pass"
            ]),
            markdown_cell([
                "---\n",
                "## Best Practices\n",
                "\n",
                "**TODO:** List best practices and common pitfalls to avoid."
            ]),
            markdown_cell([
                "---\n",
                "## 💡 Key Takeaways\n",
                "\n",
                "**TODO:** Summarize main points:\n",
                "- Point 1\n",
                "- Point 2\n",
                "- Point 3\n",
                "\n",
                "---"
            ]),
            markdown_cell([
                "## ✍️ Practice Exercises\n",
                "\n",
                "Complete these exercises to reinforce your learning:"
            ]),
            markdown_cell([
                "**Exercise 1:** TODO: Add exercise description"
            ]),
            code_cell([
                "# Write your code here\n"
            ]),
            markdown_cell([
                "**Exercise 2:** TODO: Add exercise description"
            ]),
            code_cell([
                "# Write your code here\n"
            ]),
            markdown_cell([
                "**Exercise 3:** TODO: Add exercise description"
            ]),
            code_cell([
                "# Write your code here\n"
            ]),
            markdown_cell([
                "---\n",
                "## 📚 Additional Resources\n",
                "\n",
                "**TODO:** Add links to documentation, tutorials, and further reading."
            ])
        ]
    }


def get_lesson_topics(filename):
    """Get brief topic description for each lesson."""
    topics = {
        "01_classes_deep_dive.ipynb": "class design, instance vs class attributes and methods",
        "02_inheritance_polymorphism.ipynb": "inheritance hierarchies, method overriding, and polymorphism",
        "03_encapsulation_abstraction.ipynb": "data hiding, property decorators, and abstraction",
        "04_magic_methods.ipynb": "special methods and operator overloading",
        "05_list_comprehensions.ipynb": "concise list creation and nested comprehensions",
        "06_dict_set_comprehensions.ipynb": "dictionary and set comprehensions",
        "07_generators_iterators.ipynb": "memory-efficient iteration with generators and yield",
        "08_collections_module.ipynb": "specialized container datatypes from collections",
        "09_lambda_functions.ipynb": "anonymous functions and functional programming tools",
        "10_decorators_basics.ipynb": "function wrapping and decorator syntax",
        "11_advanced_decorators.ipynb": "decorators with arguments and class decorators",
        "12_advanced_file_handling.ipynb": "context managers, binary files, and advanced I/O",
        "13_json_handling.ipynb": "JSON parsing, serialization, and API data handling",
        "14_csv_excel_operations.ipynb": "working with CSV files and spreadsheet data",
        "15_pickle_serialization.ipynb": "object serialization and persistence",
        "16_advanced_exceptions.ipynb": "custom exceptions and exception hierarchies",
        "17_logging_debugging.ipynb": "logging best practices and debugging techniques",
        "18_testing_basics.ipynb": "unit testing with unittest and pytest",
        "19_http_requests.ipynb": "making HTTP requests and working with REST APIs",
        "20_web_scraping.ipynb": "extracting data from websites with BeautifulSoup",
        "21_rest_api_basics.ipynb": "REST principles and consuming web APIs",
        "22_regex_fundamentals.ipynb": "pattern matching and text searching with regex",
        "23_regex_advanced.ipynb": "advanced regex patterns and substitutions",
        "24_virtual_environments.ipynb": "managing dependencies with venv and pip",
        "25_package_management.ipynb": "creating and distributing Python packages",
        "26_context_managers.ipynb": "implementing context managers with __enter__ and __exit__",
        "27_metaclasses_intro.ipynb": "understanding metaclasses and the type system",
        "28_type_hints.ipynb": "static type checking with type annotations",
        "29_intermediate_exercises.ipynb": "comprehensive practice problems",
        "30_intermediate_projects.ipynb": "building intermediate-level applications",
    }
    return topics.get(filename, "intermediate Python concepts")


def main():
    """Generate all intermediate course notebooks."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    intermediate_dir = project_root / "02-intermediate"
    
    # Ensure directory exists
    intermediate_dir.mkdir(exist_ok=True)
    
    print(f"Generating {len(LESSONS)} Jupyter notebooks for Intermediate course...")
    print()
    
    for filename, (title, module) in LESSONS.items():
        topics = get_lesson_topics(filename)
        lesson_data = create_lesson_template(title, module, topics)
        notebook = create_notebook_structure(lesson_data["title"], lesson_data["cells"])
        filepath = intermediate_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=2, ensure_ascii=False)
        
        print(f"  ✓ Created: {filename}")
    
    print()
    print(f"✅ Successfully generated {len(LESSONS)} notebooks in {intermediate_dir}")
    print(f"\nTo view: jupyter notebook {intermediate_dir}")


if __name__ == "__main__":
    main()
