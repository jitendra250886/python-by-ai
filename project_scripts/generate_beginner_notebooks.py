#!/usr/bin/env python3
"""
Generate Jupyter notebook files for the beginner Python course.
This script creates structured notebooks with explanations, code examples, and exercises.
"""

import json
from pathlib import Path
from datetime import datetime


# Notebook structure template
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


# Lesson content definitions
LESSONS = {
    "01_introduction_to_python.ipynb": {
        "title": "Lesson 1: Introduction to Python",
        "cells": [
            markdown_cell([
                "# Lesson 1: Introduction to Python\n",
                "\n",
                "## Welcome to Python Programming! 🐍\n",
                "\n",
                "### What is Python?\n",
                "Python is a high-level, interpreted programming language known for:\n",
                "- **Easy to learn**: Clean and readable syntax\n",
                "- **Versatile**: Web development, data science, AI, automation, and more\n",
                "- **Large community**: Extensive libraries and support\n",
                "- **Cross-platform**: Works on Windows, Mac, and Linux\n",
                "\n",
                "### Why Learn Python?\n",
                "1. Beginner-friendly syntax\n",
                "2. High demand in job market\n",
                "3. Powerful libraries for any task\n",
                "4. Great for rapid prototyping\n",
                "\n",
                "---"
            ]),
            markdown_cell([
                "## Your First Python Program\n",
                "\n",
                "Let's write the classic \"Hello, World!\" program:"
            ]),
            code_cell([
                "# This is a comment - Python ignores it\n",
                "print(\"Hello, World!\")"
            ]),
            markdown_cell([
                "**Try it yourself!** Modify the message above and run the cell again.\n",
                "\n",
                "---"
            ]),
            markdown_cell([
                "## Basic Print Statements\n",
                "\n",
                "The `print()` function displays output to the screen:"
            ]),
            code_cell([
                "# Printing different types of content\n",
                "print(\"Welcome to Python!\")\n",
                "print(42)\n",
                "print(3.14)\n",
                "print(True)"
            ]),
            markdown_cell([
                "## Multiple Print Statements"
            ]),
            code_cell([
                "print(\"Line 1\")\n",
                "print(\"Line 2\")\n",
                "print(\"Line 3\")"
            ]),
            markdown_cell([
                "## Print with Multiple Arguments"
            ]),
            code_cell([
                "# Print multiple items separated by space\n",
                "print(\"My name is\", \"Python\", \"and I am\", 33, \"years old\")"
            ]),
            markdown_cell([
                "---\n",
                "## 💡 Key Takeaways\n",
                "\n",
                "- Python is easy to learn and widely used\n",
                "- `print()` displays output\n",
                "- Comments start with `#`\n",
                "- You can print text, numbers, and more\n",
                "\n",
                "---"
            ]),
            markdown_cell([
                "## ✍️ Practice Exercises\n",
                "\n",
                "Try these exercises to reinforce what you've learned:"
            ]),
            markdown_cell([
                "**Exercise 1:** Print your name"
            ]),
            code_cell([
                "# Write your code here\n"
            ]),
            markdown_cell([
                "**Exercise 2:** Print your age and favorite hobby on the same line"
            ]),
            code_cell([
                "# Write your code here\n"
            ]),
            markdown_cell([
                "**Exercise 3:** Print a simple pattern using multiple print statements:\n",
                "```\n",
                "*\n",
                "**\n",
                "***\n",
                "```"
            ]),
            code_cell([
                "# Write your code here\n"
            ])
        ]
    },
    
    "02_variables_and_data_types.ipynb": {
        "title": "Lesson 2: Variables and Data Types",
        "cells": [
            markdown_cell([
                "# Lesson 2: Variables and Data Types\n",
                "\n",
                "## What are Variables?\n",
                "\n",
                "Variables are containers for storing data values. Think of them as labeled boxes where you can store information.\n",
                "\n",
                "### Variable Naming Rules:\n",
                "- Must start with a letter or underscore\n",
                "- Can contain letters, numbers, and underscores\n",
                "- Case-sensitive (`name` and `Name` are different)\n",
                "- Cannot use Python keywords (like `print`, `if`, `for`)\n",
                "\n",
                "---"
            ]),
            markdown_cell([
                "## Creating Variables"
            ]),
            code_cell([
                "# Creating variables\n",
                "name = \"Alice\"\n",
                "age = 25\n",
                "height = 5.6\n",
                "is_student = True\n",
                "\n",
                "print(\"Name:\", name)\n",
                "print(\"Age:\", age)\n",
                "print(\"Height:\", height)\n",
                "print(\"Is student:\", is_student)"
            ]),
            markdown_cell([
                "## Python Data Types\n",
                "\n",
                "Python has several built-in data types:\n",
                "\n",
                "| Data Type | Description | Example |\n",
                "|-----------|-------------|----------|\n",
                "| `int` | Integer numbers | `42`, `-10`, `0` |\n",
                "| `float` | Decimal numbers | `3.14`, `-0.5`, `2.0` |\n",
                "| `str` | Text/strings | `\"Hello\"`, `'Python'` |\n",
                "| `bool` | True/False values | `True`, `False` |\n",
                "\n",
                "---"
            ]),
            markdown_cell([
                "## Working with Integers (int)"
            ]),
            code_cell([
                "# Integer examples\n",
                "score = 100\n",
                "temperature = -5\n",
                "year = 2024\n",
                "\n",
                "print(\"Score:\", score)\n",
                "print(\"Type:\", type(score))"
            ]),
            markdown_cell([
                "## Working with Floats (float)"
            ]),
            code_cell([
                "# Float examples\n",
                "pi = 3.14159\n",
                "price = 19.99\n",
                "weight = 68.5\n",
                "\n",
                "print(\"Pi:\", pi)\n",
                "print(\"Type:\", type(pi))"
            ]),
            markdown_cell([
                "## Working with Strings (str)"
            ]),
            code_cell([
                "# String examples\n",
                "greeting = \"Hello, World!\"\n",
                "language = 'Python'\n",
                "message = \"\"\"This is a\n",
                "multi-line string\"\"\"\n",
                "\n",
                "print(greeting)\n",
                "print(\"Type:\", type(greeting))"
            ]),
            markdown_cell([
                "## Working with Booleans (bool)"
            ]),
            code_cell([
                "# Boolean examples\n",
                "is_sunny = True\n",
                "is_raining = False\n",
                "\n",
                "print(\"Is sunny:\", is_sunny)\n",
                "print(\"Type:\", type(is_sunny))"
            ]),
            markdown_cell([
                "## Type Conversion\n",
                "\n",
                "You can convert between data types:"
            ]),
            code_cell([
                "# Type conversion examples\n",
                "num_str = \"100\"\n",
                "num_int = int(num_str)  # String to integer\n",
                "print(\"Converted:\", num_int, \"Type:\", type(num_int))\n",
                "\n",
                "num_float = float(num_str)  # String to float\n",
                "print(\"Converted:\", num_float, \"Type:\", type(num_float))\n",
                "\n",
                "age = 25\n",
                "age_str = str(age)  # Integer to string\n",
                "print(\"Converted:\", age_str, \"Type:\", type(age_str))"
            ]),
            markdown_cell([
                "## Variable Reassignment"
            ]),
            code_cell([
                "# Variables can be reassigned\n",
                "x = 10\n",
                "print(\"Initial value:\", x)\n",
                "\n",
                "x = 20\n",
                "print(\"New value:\", x)\n",
                "\n",
                "x = \"Now I'm a string!\"\n",
                "print(\"Changed type:\", x)"
            ]),
            markdown_cell([
                "---\n",
                "## 💡 Key Takeaways\n",
                "\n",
                "- Variables store data values\n",
                "- Python has main data types: int, float, str, bool\n",
                "- Use `type()` to check data type\n",
                "- Variables can be reassigned to different values and types\n",
                "- Type conversion: `int()`, `float()`, `str()`\n",
                "\n",
                "---"
            ]),
            markdown_cell([
                "## ✍️ Practice Exercises"
            ]),
            markdown_cell([
                "**Exercise 1:** Create variables for your personal information (name, age, height, city)"
            ]),
            code_cell([
                "# Write your code here\n"
            ]),
            markdown_cell([
                "**Exercise 2:** Convert the string \"3.14\" to a float and store it in a variable"
            ]),
            code_cell([
                "# Write your code here\n"
            ]),
            markdown_cell([
                "**Exercise 3:** Create a variable with value 100, then reassign it to your name"
            ]),
            code_cell([
                "# Write your code here\n"
            ])
        ]
    },
    
    "03_basic_operators.ipynb": {
        "title": "Lesson 3: Basic Operators",
        "cells": [
            markdown_cell([
                "# Lesson 3: Basic Operators\n",
                "\n",
                "Operators are symbols that perform operations on variables and values.\n",
                "\n",
                "## Types of Operators:\n",
                "1. Arithmetic Operators\n",
                "2. Comparison Operators\n",
                "3. Logical Operators\n",
                "\n",
                "---"
            ]),
            markdown_cell([
                "## Arithmetic Operators\n",
                "\n",
                "Used to perform mathematical operations:\n",
                "\n",
                "| Operator | Description | Example |\n",
                "|----------|-------------|----------|\n",
                "| `+` | Addition | `5 + 3 = 8` |\n",
                "| `-` | Subtraction | `5 - 3 = 2` |\n",
                "| `*` | Multiplication | `5 * 3 = 15` |\n",
                "| `/` | Division | `6 / 3 = 2.0` |\n",
                "| `//` | Floor Division | `7 // 3 = 2` |\n",
                "| `%` | Modulus (remainder) | `7 % 3 = 1` |\n",
                "| `**` | Exponentiation | `2 ** 3 = 8` |"
            ]),
            code_cell([
                "# Arithmetic operations\n",
                "a = 10\n",
                "b = 3\n",
                "\n",
                "print(\"Addition:\", a + b)\n",
                "print(\"Subtraction:\", a - b)\n",
                "print(\"Multiplication:\", a * b)\n",
                "print(\"Division:\", a / b)\n",
                "print(\"Floor Division:\", a // b)\n",
                "print(\"Modulus:\", a % b)\n",
                "print(\"Exponentiation:\", a ** b)"
            ]),
            markdown_cell([
                "## Comparison Operators\n",
                "\n",
                "Used to compare values, returns True or False:\n",
                "\n",
                "| Operator | Description | Example |\n",
                "|----------|-------------|----------|\n",
                "| `==` | Equal to | `5 == 5` → True |\n",
                "| `!=` | Not equal to | `5 != 3` → True |\n",
                "| `>` | Greater than | `5 > 3` → True |\n",
                "| `<` | Less than | `5 < 3` → False |\n",
                "| `>=` | Greater than or equal | `5 >= 5` → True |\n",
                "| `<=` | Less than or equal | `3 <= 5` → True |"
            ]),
            code_cell([
                "# Comparison operations\n",
                "x = 10\n",
                "y = 5\n",
                "\n",
                "print(\"x == y:\", x == y)\n",
                "print(\"x != y:\", x != y)\n",
                "print(\"x > y:\", x > y)\n",
                "print(\"x < y:\", x < y)\n",
                "print(\"x >= y:\", x >= y)\n",
                "print(\"x <= y:\", x <= y)"
            ]),
            markdown_cell([
                "## Logical Operators\n",
                "\n",
                "Used to combine conditional statements:\n",
                "\n",
                "| Operator | Description | Example |\n",
                "|----------|-------------|----------|\n",
                "| `and` | Returns True if both are true | `True and True` → True |\n",
                "| `or` | Returns True if one is true | `True or False` → True |\n",
                "| `not` | Reverses the result | `not True` → False |"
            ]),
            code_cell([
                "# Logical operations\n",
                "p = True\n",
                "q = False\n",
                "\n",
                "print(\"p and q:\", p and q)\n",
                "print(\"p or q:\", p or q)\n",
                "print(\"not p:\", not p)\n",
                "print(\"not q:\", not q)"
            ]),
            markdown_cell([
                "## Practical Examples"
            ]),
            code_cell([
                "# Calculate area of a rectangle\n",
                "length = 10\n",
                "width = 5\n",
                "area = length * width\n",
                "print(\"Area of rectangle:\", area)"
            ]),
            code_cell([
                "# Check if a number is even or odd\n",
                "number = 7\n",
                "is_even = (number % 2 == 0)\n",
                "print(f\"Is {number} even?\", is_even)"
            ]),
            code_cell([
                "# Check age eligibility\n",
                "age = 20\n",
                "has_id = True\n",
                "can_enter = (age >= 18) and has_id\n",
                "print(\"Can enter:\", can_enter)"
            ]),
            markdown_cell([
                "## Operator Precedence\n",
                "\n",
                "Operators are evaluated in this order:\n",
                "1. `**` (Exponentiation)\n",
                "2. `*`, `/`, `//`, `%` (Multiplication, Division)\n",
                "3. `+`, `-` (Addition, Subtraction)\n",
                "4. Comparison operators\n",
                "5. Logical operators\n",
                "\n",
                "Use parentheses `()` to control order!"
            ]),
            code_cell([
                "# Without parentheses\n",
                "result1 = 5 + 3 * 2\n",
                "print(\"5 + 3 * 2 =\", result1)  # 11 (multiplication first)\n",
                "\n",
                "# With parentheses\n",
                "result2 = (5 + 3) * 2\n",
                "print(\"(5 + 3) * 2 =\", result2)  # 16 (addition first)"
            ]),
            markdown_cell([
                "---\n",
                "## 💡 Key Takeaways\n",
                "\n",
                "- Arithmetic operators: +, -, *, /, //, %, **\n",
                "- Comparison operators: ==, !=, >, <, >=, <=\n",
                "- Logical operators: and, or, not\n",
                "- Use parentheses to control operation order\n",
                "\n",
                "---"
            ]),
            markdown_cell([
                "## ✍️ Practice Exercises"
            ]),
            markdown_cell([
                "**Exercise 1:** Calculate the average of three numbers: 25, 30, 35"
            ]),
            code_cell([
                "# Write your code here\n"
            ]),
            markdown_cell([
                "**Exercise 2:** Check if a number is divisible by both 3 and 5"
            ]),
            code_cell([
                "# Write your code here (use number 15)\n"
            ]),
            markdown_cell([
                "**Exercise 3:** Calculate the final price after 20% discount on $100"
            ]),
            code_cell([
                "# Write your code here\n"
            ])
        ]
    }
}


def generate_remaining_lessons():
    """Generate templates for remaining lessons (04-20)."""
    remaining = {
        "04_conditional_statements.ipynb": "Lesson 4: Conditional Statements (if, elif, else)",
        "05_loops_part1.ipynb": "Lesson 5: For Loops and Iteration",
        "06_loops_part2.ipynb": "Lesson 6: While Loops and Loop Control",
        "07_lists.ipynb": "Lesson 7: Lists - Creation, Indexing, and Methods",
        "08_tuples.ipynb": "Lesson 8: Tuples and Immutability",
        "09_dictionaries.ipynb": "Lesson 9: Dictionaries - Key-Value Pairs",
        "10_sets.ipynb": "Lesson 10: Sets and Set Operations",
        "11_functions_basics.ipynb": "Lesson 11: Functions Basics",
        "12_function_scope.ipynb": "Lesson 12: Function Scope",
        "13_advanced_functions.ipynb": "Lesson 13: Advanced Functions",
        "14_string_manipulation.ipynb": "Lesson 14: String Manipulation",
        "15_file_handling.ipynb": "Lesson 15: File Handling",
        "16_error_handling.ipynb": "Lesson 16: Error Handling",
        "17_classes_and_objects.ipynb": "Lesson 17: Classes and Objects",
        "18_oop_fundamentals.ipynb": "Lesson 18: OOP Fundamentals",
        "19_coding_exercises.ipynb": "Lesson 19: Coding Exercises",
        "20_beginner_projects.ipynb": "Lesson 20: Beginner Projects"
    }
    
    templates = {}
    for filename, title in remaining.items():
        templates[filename] = {
            "title": title,
            "cells": [
                markdown_cell(f"# {title}\n\n**TODO:** Content to be added.\n\nThis notebook will cover:\n- Core concepts\n- Code examples\n- Practice exercises"),
                code_cell("# Example code cell\nprint(\"Coming soon!\")")
            ]
        }
    return templates


def main():
    """Generate all beginner course notebooks."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    beginner_dir = project_root / "01-beginner"
    
    # Ensure directory exists
    beginner_dir.mkdir(exist_ok=True)
    
    # Combine detailed and template lessons
    all_lessons = {**LESSONS, **generate_remaining_lessons()}
    
    print(f"Generating {len(all_lessons)} Jupyter notebooks...")
    
    for filename, lesson_data in all_lessons.items():
        notebook = create_notebook_structure(lesson_data["title"], lesson_data["cells"])
        filepath = beginner_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=2, ensure_ascii=False)
        
        print(f"  ✓ Created: {filename}")
    
    print(f"\n✅ Successfully generated {len(all_lessons)} notebooks in {beginner_dir}")
    print(f"\nTo view: jupyter notebook {beginner_dir}")


if __name__ == "__main__":
    main()
