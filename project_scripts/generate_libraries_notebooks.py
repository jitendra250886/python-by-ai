"""
Generate Jupyter Notebooks for Python Libraries & Frameworks Course (04-libraries)
This script creates 55 comprehensive Jupyter notebooks covering major Python libraries.
"""

import json
import os
from pathlib import Path

# Define the course structure
COURSE_MODULES = [
    {
        "module_name": "Data Science & Analysis",
        "lessons": [
            {
                "number": "01",
                "title": "numpy_fundamentals",
                "display_title": "NumPy Fundamentals",
                "description": "Arrays, operations, broadcasting, mathematical functions",
                "library": "numpy"
            },
            {
                "number": "02",
                "title": "pandas_data_manipulation",
                "display_title": "Pandas Data Manipulation",
                "description": "DataFrames, Series, data cleaning, filtering",
                "library": "pandas"
            },
            {
                "number": "03",
                "title": "pandas_advanced",
                "display_title": "Advanced Pandas",
                "description": "Merging, grouping, pivot tables, time series",
                "library": "pandas"
            },
            {
                "number": "04",
                "title": "matplotlib_visualization",
                "display_title": "Matplotlib Visualization",
                "description": "Plots, charts, customization, subplots",
                "library": "matplotlib"
            },
            {
                "number": "05",
                "title": "seaborn_advanced_viz",
                "display_title": "Seaborn Advanced Visualization",
                "description": "Statistical visualizations, themes, complex plots",
                "library": "seaborn"
            }
        ]
    },
    {
        "module_name": "Machine Learning Basics",
        "lessons": [
            {
                "number": "06",
                "title": "scikit_learn_intro",
                "display_title": "Introduction to Scikit-learn",
                "description": "ML basics, supervised/unsupervised learning",
                "library": "scikit-learn"
            },
            {
                "number": "07",
                "title": "scikit_learn_classification",
                "display_title": "Classification with Scikit-learn",
                "description": "Classification algorithms, model evaluation",
                "library": "scikit-learn"
            },
            {
                "number": "08",
                "title": "scikit_learn_regression",
                "display_title": "Regression with Scikit-learn",
                "description": "Regression models, feature engineering",
                "library": "scikit-learn"
            },
            {
                "number": "09",
                "title": "scikit_learn_clustering",
                "display_title": "Clustering Algorithms",
                "description": "K-means, hierarchical clustering, DBSCAN",
                "library": "scikit-learn"
            },
            {
                "number": "10",
                "title": "model_evaluation_tuning",
                "display_title": "Model Evaluation and Tuning",
                "description": "Cross-validation, grid search, metrics",
                "library": "scikit-learn"
            }
        ]
    },
    {
        "module_name": "Deep Learning Frameworks",
        "lessons": [
            {
                "number": "11",
                "title": "tensorflow_basics",
                "display_title": "TensorFlow Basics",
                "description": "Tensors, operations, computational graphs",
                "library": "tensorflow"
            },
            {
                "number": "12",
                "title": "keras_neural_networks",
                "display_title": "Keras Neural Networks",
                "description": "Sequential models, layers, training",
                "library": "keras"
            },
            {
                "number": "13",
                "title": "pytorch_fundamentals",
                "display_title": "PyTorch Fundamentals",
                "description": "Tensors, autograd, building models",
                "library": "pytorch"
            },
            {
                "number": "14",
                "title": "cnn_image_classification",
                "display_title": "CNN for Image Classification",
                "description": "Convolutional networks for images",
                "library": "tensorflow/pytorch"
            },
            {
                "number": "15",
                "title": "transfer_learning",
                "display_title": "Transfer Learning",
                "description": "Pre-trained models, fine-tuning",
                "library": "tensorflow/pytorch"
            }
        ]
    },
    {
        "module_name": "Natural Language Processing",
        "lessons": [
            {
                "number": "16",
                "title": "nltk_text_processing",
                "display_title": "NLTK Text Processing",
                "description": "Tokenization, stemming, lemmatization, POS tagging",
                "library": "nltk"
            },
            {
                "number": "17",
                "title": "spacy_nlp",
                "display_title": "spaCy for NLP",
                "description": "Named entity recognition, dependency parsing, pipelines",
                "library": "spacy"
            },
            {
                "number": "18",
                "title": "text_classification_sentiment",
                "display_title": "Text Classification and Sentiment Analysis",
                "description": "Sentiment analysis, text classification",
                "library": "nltk/spacy/scikit-learn"
            }
        ]
    },
    {
        "module_name": "Web Development",
        "lessons": [
            {
                "number": "19",
                "title": "flask_basics",
                "display_title": "Flask Basics",
                "description": "Routes, templates, request handling",
                "library": "flask"
            },
            {
                "number": "20",
                "title": "flask_rest_api",
                "display_title": "Building REST APIs with Flask",
                "description": "Building RESTful APIs, JSON responses",
                "library": "flask"
            },
            {
                "number": "21",
                "title": "django_introduction",
                "display_title": "Introduction to Django",
                "description": "MVC/MTV architecture, models, views, templates",
                "library": "django"
            },
            {
                "number": "22",
                "title": "fastapi_modern_apis",
                "display_title": "Modern APIs with FastAPI",
                "description": "Async APIs, automatic documentation, Pydantic",
                "library": "fastapi"
            },
            {
                "number": "23",
                "title": "streamlit_data_apps",
                "display_title": "Data Apps with Streamlit",
                "description": "Interactive dashboards, widgets, data visualization",
                "library": "streamlit"
            }
        ]
    },
    {
        "module_name": "Web Scraping & Automation",
        "lessons": [
            {
                "number": "24",
                "title": "requests_http",
                "display_title": "HTTP Requests with Requests",
                "description": "HTTP requests, APIs, authentication",
                "library": "requests"
            },
            {
                "number": "25",
                "title": "beautifulsoup_scraping",
                "display_title": "Web Scraping with Beautiful Soup",
                "description": "Parsing HTML, extracting data, navigation",
                "library": "beautifulsoup4"
            },
            {
                "number": "26",
                "title": "selenium_automation",
                "display_title": "Browser Automation with Selenium",
                "description": "Browser automation, form filling, dynamic content",
                "library": "selenium"
            },
            {
                "number": "27",
                "title": "pyautogui_gui_automation",
                "display_title": "GUI Automation with PyAutoGUI",
                "description": "Mouse/keyboard control, screenshots",
                "library": "pyautogui"
            }
        ]
    },
    {
        "module_name": "Image Processing & Computer Vision",
        "lessons": [
            {
                "number": "28",
                "title": "pillow_image_basics",
                "display_title": "Image Basics with Pillow",
                "description": "Opening, editing, filters, transformations",
                "library": "pillow"
            },
            {
                "number": "29",
                "title": "opencv_fundamentals",
                "display_title": "OpenCV Fundamentals",
                "description": "Reading videos, image operations, drawing",
                "library": "opencv-python"
            },
            {
                "number": "30",
                "title": "opencv_computer_vision",
                "display_title": "Computer Vision with OpenCV",
                "description": "Edge detection, contours, feature matching",
                "library": "opencv-python"
            },
            {
                "number": "31",
                "title": "face_detection_recognition",
                "display_title": "Face Detection and Recognition",
                "description": "Haar cascades, face recognition algorithms",
                "library": "opencv-python"
            }
        ]
    },
    {
        "module_name": "Scientific Computing",
        "lessons": [
            {
                "number": "32",
                "title": "scipy_scientific_tools",
                "display_title": "SciPy Scientific Tools",
                "description": "Optimization, integration, interpolation",
                "library": "scipy"
            },
            {
                "number": "33",
                "title": "sympy_symbolic_math",
                "display_title": "Symbolic Mathematics with SymPy",
                "description": "Symbolic mathematics, equations, calculus",
                "library": "sympy"
            },
            {
                "number": "34",
                "title": "statistics_data_analysis",
                "display_title": "Statistics and Data Analysis",
                "description": "Statistical tests, distributions, hypothesis testing",
                "library": "scipy/statsmodels"
            }
        ]
    },
    {
        "module_name": "Desktop & GUI Development",
        "lessons": [
            {
                "number": "35",
                "title": "tkinter_gui_basics",
                "display_title": "GUI Basics with Tkinter",
                "description": "Widgets, layout managers, event handling",
                "library": "tkinter"
            },
            {
                "number": "36",
                "title": "pyqt_desktop_apps",
                "display_title": "Desktop Apps with PyQt",
                "description": "Qt framework, signals/slots, modern UIs",
                "library": "PyQt5"
            },
            {
                "number": "37",
                "title": "kivy_cross_platform",
                "display_title": "Cross-Platform Apps with Kivy",
                "description": "Mobile and desktop apps, touch interfaces",
                "library": "kivy"
            }
        ]
    },
    {
        "module_name": "Database & Data Storage",
        "lessons": [
            {
                "number": "38",
                "title": "sqlite_database",
                "display_title": "SQLite Database",
                "description": "SQL basics, CRUD operations, Python integration",
                "library": "sqlite3"
            },
            {
                "number": "39",
                "title": "sqlalchemy_orm",
                "display_title": "SQLAlchemy ORM",
                "description": "Object-relational mapping, models, queries",
                "library": "sqlalchemy"
            },
            {
                "number": "40",
                "title": "redis_caching",
                "display_title": "Redis for Caching",
                "description": "Key-value store, caching, pub/sub",
                "library": "redis"
            }
        ]
    },
    {
        "module_name": "Testing & Quality",
        "lessons": [
            {
                "number": "41",
                "title": "pytest_testing",
                "display_title": "Testing with Pytest",
                "description": "Unit tests, fixtures, parametrization",
                "library": "pytest"
            },
            {
                "number": "42",
                "title": "unittest_mocking",
                "display_title": "Unittest and Mocking",
                "description": "Test suites, mocking, assertions",
                "library": "unittest"
            },
            {
                "number": "43",
                "title": "code_quality_tools",
                "display_title": "Code Quality Tools",
                "description": "Linting (pylint, flake8), formatting (black), type checking (mypy)",
                "library": "pylint/flake8/black/mypy"
            }
        ]
    },
    {
        "module_name": "Data Formats & Serialization",
        "lessons": [
            {
                "number": "44",
                "title": "json_xml_parsing",
                "display_title": "JSON and XML Parsing",
                "description": "Working with JSON and XML data",
                "library": "json/xml"
            },
            {
                "number": "45",
                "title": "yaml_config_files",
                "display_title": "YAML Configuration Files",
                "description": "Configuration management, YAML parsing",
                "library": "pyyaml"
            },
            {
                "number": "46",
                "title": "protobuf_serialization",
                "display_title": "Protocol Buffers Serialization",
                "description": "Protocol buffers, efficient data exchange",
                "library": "protobuf"
            }
        ]
    },
    {
        "module_name": "Async & Concurrency",
        "lessons": [
            {
                "number": "47",
                "title": "asyncio_basics",
                "display_title": "Asyncio Basics",
                "description": "Async/await, coroutines, event loops",
                "library": "asyncio"
            },
            {
                "number": "48",
                "title": "aiohttp_async_requests",
                "display_title": "Async HTTP with Aiohttp",
                "description": "Async HTTP client/server",
                "library": "aiohttp"
            },
            {
                "number": "49",
                "title": "celery_task_queues",
                "display_title": "Task Queues with Celery",
                "description": "Distributed task processing, scheduling",
                "library": "celery"
            }
        ]
    },
    {
        "module_name": "DevOps & Deployment",
        "lessons": [
            {
                "number": "50",
                "title": "docker_python_apps",
                "display_title": "Docker for Python Apps",
                "description": "Containerization, Dockerfile, docker-compose",
                "library": "docker"
            },
            {
                "number": "51",
                "title": "logging_monitoring",
                "display_title": "Logging and Monitoring",
                "description": "Logging module, structured logging, monitoring",
                "library": "logging"
            },
            {
                "number": "52",
                "title": "deployment_best_practices",
                "display_title": "Deployment Best Practices",
                "description": "Production deployment, environment management",
                "library": "various"
            }
        ]
    },
    {
        "module_name": "Specialized Libraries",
        "lessons": [
            {
                "number": "53",
                "title": "plotly_interactive_viz",
                "display_title": "Interactive Visualization with Plotly",
                "description": "Interactive charts, dashboards, Plotly Express",
                "library": "plotly"
            },
            {
                "number": "54",
                "title": "geopy_location_data",
                "display_title": "Location Data with Geopy",
                "description": "Geocoding, distance calculation, maps",
                "library": "geopy"
            },
            {
                "number": "55",
                "title": "schedule_task_automation",
                "display_title": "Task Automation with Schedule",
                "description": "Job scheduling, periodic tasks",
                "library": "schedule"
            }
        ]
    }
]


def create_notebook_content(lesson_number, title, display_title, description, library, module_name):
    """
    Create comprehensive Jupyter notebook content for a library lesson.
    """
    notebook = {
        "cells": [
            # Title cell
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Lesson {lesson_number}: {display_title}\n",
                    "\n",
                    f"**Module:** {module_name}  \n",
                    f"**Library:** {library}  \n",
                    f"**Description:** {description}\n",
                    "\n",
                    "---\n"
                ]
            },
            # Learning Objectives
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 📋 Learning Objectives\n",
                    "\n",
                    "By the end of this lesson, you will be able to:\n",
                    "- Understand the purpose and key features of the library\n",
                    "- Install and import the library correctly\n",
                    "- Use core functions and classes\n",
                    "- Apply the library to solve real-world problems\n",
                    "- Follow best practices and common patterns\n",
                    "\n",
                    "---\n"
                ]
            },
            # Prerequisites
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 📚 Prerequisites\n",
                    "\n",
                    "Before starting this lesson, make sure you have:\n",
                    "- Python 3.8+ installed\n",
                    "- Basic understanding of Python fundamentals\n",
                    "- Completed previous lessons in the course (if applicable)\n",
                    "- A code editor or Jupyter environment set up\n",
                    "\n",
                    "---\n"
                ]
            },
            # Installation
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## ⚙️ Installation\n",
                    "\n",
                    f"To install {library}, run the following command:\n",
                    "\n",
                    "```bash\n",
                    f"pip install {library}\n",
                    "```\n",
                    "\n",
                    "**Note:** Some libraries may have additional dependencies or specific installation instructions. Check the official documentation if you encounter issues.\n",
                    "\n",
                    "---\n"
                ]
            },
            # Import code cell
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Import required libraries\n",
                    f"# import {library.replace('-', '_')}\n",
                    "\n",
                    "# Standard library imports\n",
                    "import os\n",
                    "import sys\n",
                    "\n",
                    "print(f\"Python version: {sys.version}\")\n",
                    f"# print(f\"{library} imported successfully!\")\n"
                ]
            },
            # Introduction
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 📖 Introduction\n",
                    "\n",
                    f"### What is {display_title}?\n",
                    "\n",
                    f"{display_title} is a powerful Python library used for {description.lower()}. This lesson will cover the fundamental concepts, practical examples, and best practices for using this library effectively.\n",
                    "\n",
                    "### Key Features:\n",
                    "- Feature 1: [To be filled with specific library features]\n",
                    "- Feature 2: [To be filled with specific library features]\n",
                    "- Feature 3: [To be filled with specific library features]\n",
                    "\n",
                    "### Common Use Cases:\n",
                    "- Use case 1\n",
                    "- Use case 2\n",
                    "- Use case 3\n",
                    "\n",
                    "---\n"
                ]
            },
            # Core Concepts Section 1
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 🔑 Core Concept 1: [Basic Operations]\n",
                    "\n",
                    "Description of the first core concept goes here.\n",
                    "\n",
                    "### Example:\n"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example code for Core Concept 1\n",
                    "# This section will contain practical examples\n",
                    "\n",
                    "# Example 1: Basic usage\n",
                    "print(\"Example 1: Basic usage\")\n",
                    "\n",
                    "# Example 2: Common patterns\n",
                    "print(\"Example 2: Common patterns\")\n"
                ]
            },
            # Core Concepts Section 2
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 🔑 Core Concept 2: [Intermediate Operations]\n",
                    "\n",
                    "Description of the second core concept goes here.\n",
                    "\n",
                    "### Example:\n"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example code for Core Concept 2\n",
                    "# This section will contain intermediate examples\n",
                    "\n",
                    "# Example 1: Intermediate usage\n",
                    "print(\"Example 1: Intermediate usage\")\n",
                    "\n",
                    "# Example 2: Advanced patterns\n",
                    "print(\"Example 2: Advanced patterns\")\n"
                ]
            },
            # Core Concepts Section 3
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 🔑 Core Concept 3: [Advanced Features]\n",
                    "\n",
                    "Description of the third core concept goes here.\n",
                    "\n",
                    "### Example:\n"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Example code for Core Concept 3\n",
                    "# This section will contain advanced examples\n",
                    "\n",
                    "# Example 1: Advanced usage\n",
                    "print(\"Example 1: Advanced usage\")\n",
                    "\n",
                    "# Example 2: Complex scenarios\n",
                    "print(\"Example 2: Complex scenarios\")\n"
                ]
            },
            # Real-world Example
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 🌍 Real-World Example\n",
                    "\n",
                    f"Let's build a practical example using {display_title} that demonstrates how this library is used in real-world applications.\n",
                    "\n",
                    "### Project: [Project Name]\n",
                    "\n",
                    "**Objective:** Create a practical application that showcases the library's capabilities.\n",
                    "\n",
                    "**Steps:**\n",
                    "1. Step 1: Setup and configuration\n",
                    "2. Step 2: Implement core functionality\n",
                    "3. Step 3: Add advanced features\n",
                    "4. Step 4: Test and optimize\n"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Real-world example implementation\n",
                    "# This will be a complete, practical example\n",
                    "\n",
                    "def main():\n",
                    "    \"\"\"\n",
                    "    Main function for the real-world example.\n",
                    "    \"\"\"\n",
                    "    print(\"Real-world example implementation\")\n",
                    "    # Implementation goes here\n",
                    "    pass\n",
                    "\n",
                    "# Run the example\n",
                    "# main()\n"
                ]
            },
            # Best Practices
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## ✅ Best Practices\n",
                    "\n",
                    f"When working with {display_title}, keep these best practices in mind:\n",
                    "\n",
                    "1. **Practice 1:** Description\n",
                    "2. **Practice 2:** Description\n",
                    "3. **Practice 3:** Description\n",
                    "4. **Practice 4:** Description\n",
                    "5. **Practice 5:** Description\n",
                    "\n",
                    "### Common Pitfalls to Avoid:\n",
                    "- Pitfall 1: Description\n",
                    "- Pitfall 2: Description\n",
                    "- Pitfall 3: Description\n",
                    "\n",
                    "---\n"
                ]
            },
            # Exercises
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 🏋️ Practice Exercises\n",
                    "\n",
                    "Complete the following exercises to reinforce your understanding:\n",
                    "\n",
                    "### Exercise 1: Basic Implementation\n",
                    "**Task:** Create a simple application using the library's basic features.\n",
                    "\n",
                    "**Requirements:**\n",
                    "- Requirement 1\n",
                    "- Requirement 2\n",
                    "- Requirement 3\n",
                    "\n",
                    "### Exercise 2: Intermediate Challenge\n",
                    "**Task:** Build upon Exercise 1 by adding more complex functionality.\n",
                    "\n",
                    "**Requirements:**\n",
                    "- Requirement 1\n",
                    "- Requirement 2\n",
                    "- Requirement 3\n",
                    "\n",
                    "### Exercise 3: Advanced Project\n",
                    "**Task:** Create a complete application that demonstrates mastery of the library.\n",
                    "\n",
                    "**Requirements:**\n",
                    "- Requirement 1\n",
                    "- Requirement 2\n",
                    "- Requirement 3\n"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Exercise 1 Solution Space\n",
                    "# Write your code here\n",
                    "\n",
                    "\n"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Exercise 2 Solution Space\n",
                    "# Write your code here\n",
                    "\n",
                    "\n"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Exercise 3 Solution Space\n",
                    "# Write your code here\n",
                    "\n",
                    "\n"
                ]
            },
            # Additional Resources
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 📚 Additional Resources\n",
                    "\n",
                    f"### Official Documentation\n",
                    "- [Official {display_title} Documentation](#)\n",
                    "- [API Reference](#)\n",
                    "- [GitHub Repository](#)\n",
                    "\n",
                    "### Tutorials and Guides\n",
                    "- Tutorial 1\n",
                    "- Tutorial 2\n",
                    "- Tutorial 3\n",
                    "\n",
                    "### Community Resources\n",
                    "- Stack Overflow Questions\n",
                    "- Reddit Community\n",
                    "- Discord/Slack Channels\n",
                    "\n",
                    "### Books and Courses\n",
                    "- Recommended Book 1\n",
                    "- Online Course 1\n",
                    "- Video Tutorial Series\n",
                    "\n",
                    "---\n"
                ]
            },
            # Summary
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 🎯 Summary\n",
                    "\n",
                    "In this lesson, you learned:\n",
                    "\n",
                    f"- ✅ How to install and import {display_title}\n",
                    "- ✅ Core concepts and fundamental operations\n",
                    "- ✅ Intermediate and advanced features\n",
                    "- ✅ Real-world applications and use cases\n",
                    "- ✅ Best practices and common pitfalls\n",
                    "- ✅ How to apply the library to solve practical problems\n",
                    "\n",
                    "### Next Steps:\n",
                    "- Complete the practice exercises\n",
                    "- Explore the additional resources\n",
                    "- Move on to the next lesson in the course\n",
                    "- Build your own projects using this library\n",
                    "\n",
                    "---\n",
                    "\n",
                    "**Great job completing this lesson! 🎉**\n"
                ]
            },
            # Footer
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "---\n",
                    "\n",
                    "**Course:** Python Libraries & Frameworks Master Course  \n",
                    f"**Lesson:** {lesson_number} - {display_title}  \n",
                    "**Level:** Intermediate to Advanced  \n",
                    "\n",
                    "For questions or feedback, refer to the course documentation.\n"
                ]
            }
        ],
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
        "nbformat_minor": 4
    }
    
    return notebook


def generate_all_notebooks():
    """
    Generate all 55 Jupyter notebooks for the libraries course.
    """
    # Get the project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    output_dir = project_root / "04-libraries"
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    
    print(f"Generating notebooks in: {output_dir}")
    print("=" * 60)
    
    total_generated = 0
    
    # Generate notebooks for each module
    for module in COURSE_MODULES:
        module_name = module["module_name"]
        print(f"\n📦 Module: {module_name}")
        print("-" * 60)
        
        for lesson in module["lessons"]:
            lesson_number = lesson["number"]
            title = lesson["title"]
            display_title = lesson["display_title"]
            description = lesson["description"]
            library = lesson["library"]
            
            # Create notebook filename
            filename = f"{lesson_number}_{title}.ipynb"
            filepath = output_dir / filename
            
            # Generate notebook content
            notebook_content = create_notebook_content(
                lesson_number,
                title,
                display_title,
                description,
                library,
                module_name
            )
            
            # Write notebook to file
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(notebook_content, f, indent=2, ensure_ascii=False)
            
            print(f"  ✅ Created: {filename}")
            total_generated += 1
    
    print("\n" + "=" * 60)
    print(f"✨ Successfully generated {total_generated} notebooks!")
    print(f"📁 Location: {output_dir}")
    print("\nTo use these notebooks:")
    print("1. Navigate to the 04-libraries directory")
    print("2. Run: jupyter notebook")
    print("3. Open any .ipynb file to start learning")
    print("\nTo convert to markdown for web:")
    print("  jupyter nbconvert --to markdown <notebook_name>.ipynb")


if __name__ == "__main__":
    print("🚀 Python Libraries & Frameworks Course Generator")
    print("=" * 60)
    generate_all_notebooks()
    print("\n🎉 All notebooks generated successfully!")
