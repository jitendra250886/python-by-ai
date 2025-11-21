#!/usr/bin/env python3
"""
Generate Jupyter notebook files for the advanced Python course.
This script creates 42 structured notebooks with templates for all lessons.
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


# Lesson definitions for advanced course
LESSONS = {
    # Module 1: Advanced OOP & Design Patterns
    "01_metaclasses_advanced.ipynb": ("Lesson 1: Advanced Metaclasses", "Module 1: Advanced OOP", "metaclass programming and class factories"),
    "02_descriptors_properties.ipynb": ("Lesson 2: Descriptors & Properties", "Module 1: Advanced OOP", "descriptor protocol and property implementation"),
    "03_abstract_base_classes.ipynb": ("Lesson 3: Abstract Base Classes", "Module 1: Advanced OOP", "ABC module and interface design"),
    "04_design_patterns_creational.ipynb": ("Lesson 4: Creational Design Patterns", "Module 1: Advanced OOP", "Singleton, Factory, and Builder patterns"),
    "05_design_patterns_structural.ipynb": ("Lesson 5: Structural Design Patterns", "Module 1: Advanced OOP", "Adapter, Decorator, and Facade patterns"),
    
    # Module 2: Functional Programming Advanced
    "06_closures_scope.ipynb": ("Lesson 6: Closures & Scope", "Module 2: Functional Programming", "closures, nonlocal, and scope resolution"),
    "07_functional_tools.ipynb": ("Lesson 7: Functional Tools", "Module 2: Functional Programming", "functools, itertools, and operator modules"),
    "08_partial_curry.ipynb": ("Lesson 8: Partial Application & Currying", "Module 2: Functional Programming", "partial application, currying, and composition"),
    
    # Module 3: Concurrency & Parallelism
    "09_threading_basics.ipynb": ("Lesson 9: Threading Basics", "Module 3: Concurrency", "threading module and thread safety"),
    "10_multiprocessing.ipynb": ("Lesson 10: Multiprocessing", "Module 3: Concurrency", "process-based parallelism and Pool"),
    "11_concurrent_futures.ipynb": ("Lesson 11: Concurrent Futures", "Module 3: Concurrency", "ThreadPoolExecutor and ProcessPoolExecutor"),
    "12_asyncio_basics.ipynb": ("Lesson 12: Asyncio Basics", "Module 3: Concurrency", "async/await, event loop, and coroutines"),
    "13_asyncio_advanced.ipynb": ("Lesson 13: Asyncio Advanced", "Module 3: Concurrency", "async context managers and async generators"),
    "14_async_patterns.ipynb": ("Lesson 14: Async Patterns", "Module 3: Concurrency", "task management, gathering, and timeouts"),
    
    # Module 4: Performance Optimization
    "15_profiling_timing.ipynb": ("Lesson 15: Profiling & Timing", "Module 4: Performance", "cProfile, timeit, and memory profiling"),
    "16_optimization_techniques.ipynb": ("Lesson 16: Optimization Techniques", "Module 4: Performance", "algorithm optimization and caching"),
    "17_memory_management.ipynb": ("Lesson 17: Memory Management", "Module 4: Performance", "memory model, garbage collection, and __slots__"),
    "18_cython_numba.ipynb": ("Lesson 18: Cython & Numba", "Module 4: Performance", "code compilation and performance acceleration"),
    
    # Module 5: Advanced Data Structures
    "19_trees_graphs.ipynb": ("Lesson 19: Trees & Graphs", "Module 5: Data Structures", "tree structures and graph representations"),
    "20_heaps_priority_queues.ipynb": ("Lesson 20: Heaps & Priority Queues", "Module 5: Data Structures", "heapq module and priority queues"),
    "21_custom_data_structures.ipynb": ("Lesson 21: Custom Data Structures", "Module 5: Data Structures", "implementing custom container types"),
    
    # Module 6: Metaprogramming
    "22_introspection.ipynb": ("Lesson 22: Introspection", "Module 6: Metaprogramming", "inspect module and runtime analysis"),
    "23_dynamic_code_execution.ipynb": ("Lesson 23: Dynamic Code Execution", "Module 6: Metaprogramming", "eval, exec, and compile"),
    "24_code_generation.ipynb": ("Lesson 24: Code Generation", "Module 6: Metaprogramming", "dynamic class and function creation"),
    "25_ast_manipulation.ipynb": ("Lesson 25: AST Manipulation", "Module 6: Metaprogramming", "abstract syntax trees and code transformation"),
    
    # Module 7: Advanced I/O & Networking
    "26_async_networking.ipynb": ("Lesson 26: Async Networking", "Module 7: Networking", "async HTTP and aiohttp"),
    "27_socket_programming.ipynb": ("Lesson 27: Socket Programming", "Module 7: Networking", "TCP/UDP sockets and network protocols"),
    "28_database_async.ipynb": ("Lesson 28: Async Databases", "Module 7: Networking", "async database operations and ORMs"),
    
    # Module 8: Security & Best Practices
    "29_secure_coding.ipynb": ("Lesson 29: Secure Coding", "Module 8: Security", "input validation and injection prevention"),
    "30_cryptography_basics.ipynb": ("Lesson 30: Cryptography Basics", "Module 8: Security", "hashing, encryption, and cryptography module"),
    "31_code_security.ipynb": ("Lesson 31: Code Security", "Module 8: Security", "security auditing and common vulnerabilities"),
    
    # Module 9: Testing & Quality
    "32_advanced_testing.ipynb": ("Lesson 32: Advanced Testing", "Module 9: Testing", "mocking, fixtures, and parametrization"),
    "33_property_based_testing.ipynb": ("Lesson 33: Property-Based Testing", "Module 9: Testing", "Hypothesis and property testing"),
    "34_test_coverage_ci.ipynb": ("Lesson 34: Test Coverage & CI", "Module 9: Testing", "coverage analysis and CI/CD integration"),
    
    # Module 10: Design Patterns Behavioral
    "35_observer_strategy.ipynb": ("Lesson 35: Observer & Strategy Patterns", "Module 10: Design Patterns", "Observer and Strategy patterns"),
    "36_command_iterator.ipynb": ("Lesson 36: Command & Iterator Patterns", "Module 10: Design Patterns", "Command and Iterator patterns"),
    "37_state_template.ipynb": ("Lesson 37: State & Template Patterns", "Module 10: Design Patterns", "State and Template patterns"),
    
    # Module 11: Advanced Topics
    "38_protocols_structural.ipynb": ("Lesson 38: Protocols & Structural Subtyping", "Module 11: Advanced Topics", "structural subtyping and Protocol class"),
    "39_context_vars.ipynb": ("Lesson 39: Context Variables", "Module 11: Advanced Topics", "context variables and async context"),
    "40_advanced_packaging.ipynb": ("Lesson 40: Advanced Packaging", "Module 11: Advanced Topics", "setup.py, wheels, and PyPI publishing"),
    
    # Module 12: Projects & Practice
    "41_advanced_exercises.ipynb": ("Lesson 41: Advanced Exercises", "Module 12: Practice", "complex problem-solving exercises"),
    "42_advanced_projects.ipynb": ("Lesson 42: Advanced Projects", "Module 12: Practice", "production-grade project implementations"),
}


def create_lesson_template(title, module, lesson_topics):
    """Create a template for an advanced lesson."""
    return {
        "title": title,
        "cells": [
            markdown_cell([
                f"# {title}\n",
                f"**{module}**\n",
                "\n",
                "## Overview\n",
                f"This advanced lesson covers {lesson_topics}. You'll learn expert-level techniques and best practices used in production environments.\n",
                "\n",
                "## Topics Covered\n",
                "- Theoretical foundations\n",
                "- Advanced implementation techniques\n",
                "- Performance considerations\n",
                "- Real-world use cases\n",
                "- Industry best practices\n",
                "- Complex exercises\n",
                "\n",
                "## Prerequisites\n",
                "- Completion of Intermediate course\n",
                "- Strong Python fundamentals\n",
                "- Experience with OOP and functional programming\n",
                "\n",
                "---"
            ]),
            markdown_cell([
                "## Introduction\n",
                "\n",
                "**TODO:** Add comprehensive introduction covering theoretical background and practical relevance."
            ]),
            code_cell([
                "# Advanced example placeholder\n",
                "# TODO: Add sophisticated code examples\n",
                "\n",
                "print(\"Advanced lesson content coming soon!\")"
            ]),
            markdown_cell([
                "---\n",
                "## Core Concepts\n",
                "\n",
                "**TODO:** Deep dive into advanced concepts with detailed explanations."
            ]),
            code_cell([
                "# Concept demonstration\n",
                "pass"
            ]),
            markdown_cell([
                "---\n",
                "## Advanced Techniques\n",
                "\n",
                "**TODO:** Demonstrate expert-level techniques and patterns."
            ]),
            code_cell([
                "# Advanced technique example\n",
                "pass"
            ]),
            markdown_cell([
                "---\n",
                "## Performance Considerations\n",
                "\n",
                "**TODO:** Discuss performance implications and optimization strategies."
            ]),
            code_cell([
                "# Performance comparison example\n",
                "pass"
            ]),
            markdown_cell([
                "---\n",
                "## Real-World Applications\n",
                "\n",
                "**TODO:** Show production-grade examples and use cases."
            ]),
            code_cell([
                "# Production example placeholder\n",
                "pass"
            ]),
            markdown_cell([
                "---\n",
                "## Best Practices & Pitfalls\n",
                "\n",
                "**TODO:** List industry best practices and common mistakes to avoid.\n",
                "\n",
                "### Best Practices:\n",
                "- TBD\n",
                "\n",
                "### Common Pitfalls:\n",
                "- TBD"
            ]),
            markdown_cell([
                "---\n",
                "## 💡 Key Takeaways\n",
                "\n",
                "**TODO:** Summarize critical concepts:\n",
                "- Advanced concept 1\n",
                "- Advanced concept 2\n",
                "- Advanced concept 3\n",
                "- Performance insight\n",
                "- Best practice highlight\n",
                "\n",
                "---"
            ]),
            markdown_cell([
                "## ✍️ Advanced Exercises\n",
                "\n",
                "These exercises are designed to challenge your understanding:"
            ]),
            markdown_cell([
                "**Exercise 1 (Hard):** TODO: Add challenging exercise"
            ]),
            code_cell([
                "# Write your solution here\n"
            ]),
            markdown_cell([
                "**Exercise 2 (Hard):** TODO: Add challenging exercise"
            ]),
            code_cell([
                "# Write your solution here\n"
            ]),
            markdown_cell([
                "**Exercise 3 (Expert):** TODO: Add expert-level exercise"
            ]),
            code_cell([
                "# Write your solution here\n"
            ]),
            markdown_cell([
                "---\n",
                "## 📚 Additional Resources\n",
                "\n",
                "**TODO:** Add references to:\n",
                "- Official Python documentation\n",
                "- PEPs (Python Enhancement Proposals)\n",
                "- Academic papers\n",
                "- Production codebases\n",
                "- Advanced books and articles"
            ])
        ]
    }


def main():
    """Generate all advanced course notebooks."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    advanced_dir = project_root / "03-advanced"
    
    # Ensure directory exists
    advanced_dir.mkdir(exist_ok=True)
    
    print(f"Generating {len(LESSONS)} Jupyter notebooks for Advanced course...")
    print()
    
    for filename, (title, module, topics) in LESSONS.items():
        lesson_data = create_lesson_template(title, module, topics)
        notebook = create_notebook_structure(lesson_data["title"], lesson_data["cells"])
        filepath = advanced_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=2, ensure_ascii=False)
        
        print(f"  ✓ Created: {filename}")
    
    print()
    print(f"✅ Successfully generated {len(LESSONS)} notebooks in {advanced_dir}")
    print(f"\nTo view: jupyter notebook {advanced_dir}")


if __name__ == "__main__":
    main()
