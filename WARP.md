# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is a comprehensive Python educational course repository organized into 6 progressive levels:

- **01-beginner/**: Python fundamentals (syntax, control flow, functions, basic I/O)
- **02-intermediate/**: OOP, file handling, APIs, testing basics, virtual environments
- **03-advanced/**: Decorators, async programming, concurrency, design patterns, performance
- **04-libraries/**: Domain-specific libraries (NumPy, Pandas, Flask, Django, TensorFlow, PyTorch, etc.)
- **05-applications/**: Real-world use cases (web scraping, ML models, automation, desktop apps)
- **06-projects/**: Complete projects organized by difficulty level

Each level builds upon previous concepts. The repository contains educational materials, code examples, exercises, and hands-on projects.

## Development Commands

### Python Environment
```powershell
# Check Python version (should be 3.8+)
python --version

# Create virtual environment for a specific section/project
python -m venv venv

# Activate virtual environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Deactivate virtual environment
deactivate

# Install dependencies (when requirements.txt exists)
pip install -r requirements.txt

# Install development dependencies
pip install pytest flake8 black mypy
```

### Running Code
```powershell
# Run a Python script
python path\to\script.py

# Run a specific module
python -m module_name

# Run with verbose output for debugging
python -v script.py
```

### Testing
```powershell
# Run all tests (when pytest is configured)
pytest

# Run tests in a specific directory
pytest 01-beginner\

# Run tests with verbose output
pytest -v

# Run a single test file
pytest path\to\test_file.py

# Run tests matching a pattern
pytest -k "test_pattern"

# Run tests with coverage
pytest --cov=. --cov-report=html
```

### Code Quality
```powershell
# Format code with black (if installed)
black path\to\file.py
black .  # Format entire directory

# Check code style with flake8 (if installed)
flake8 path\to\file.py
flake8 .  # Check entire directory

# Type checking with mypy (if installed)
mypy path\to\file.py
```

## Architecture and Organization

### Directory Structure Pattern
Each level follows a similar organization:
- Numbered lessons/topics (e.g., `01-topic-name.md` or `01-topic-name.py`)
- Accompanying code examples in `.py` files
- Exercise files (often named `exercises.py` or `practice.py`)
- Project subdirectories with their own structure

### Code Examples
- **Standalone scripts**: Complete, runnable examples demonstrating specific concepts
- **Exercise templates**: Partial implementations for learners to complete
- **Project code**: Full applications organized in subdirectories with their own requirements

### Library-Specific Code (04-libraries/)
When working with library examples, note:
- Each library has its own subdirectory
- Dependencies should be installed in a virtual environment
- Examples may require specific data files or API keys
- Some libraries (TensorFlow, PyTorch) have large dependencies

### Projects (06-projects/)
Projects are organized by difficulty:
- **beginner/**: Simple console applications, basic GUI apps
- **intermediate/**: API integrations, web scrapers, data analysis
- **advanced/**: ML pipelines, real-time systems, complex architectures
- **domain-specific/**: Medical, IoT, AI/ML, computer vision projects

Each project typically has:
- Its own directory with `main.py` or similar entry point
- Local `requirements.txt` if it needs specific dependencies
- README.md explaining the project and how to run it

## Working with This Repository

### When Creating New Examples
1. Place in the appropriate level directory (01-beginner through 06-projects)
2. Use clear, descriptive filenames with numbering (e.g., `03-functions.py`)
3. Include comprehensive comments explaining concepts
4. Follow PEP 8 style guidelines
5. Add docstrings to functions and classes
6. Consider cross-platform compatibility (Windows/macOS/Linux)

### When Creating Projects
1. Create a dedicated subdirectory in the appropriate level
2. Include a project-specific README.md
3. Add requirements.txt for dependencies
4. Provide sample data files if needed (in a `data/` subdirectory)
5. Include example output or screenshots where helpful

### When Writing Tests
1. Test files should be named `test_*.py` or `*_test.py`
2. Place tests alongside the code they test or in a `tests/` subdirectory
3. Use descriptive test function names: `test_function_name_expected_behavior`
4. Include both positive and negative test cases

### Path Handling
- Use `pathlib.Path` for cross-platform file path handling
- Avoid hardcoded absolute paths
- Use relative paths from the script's location when accessing resources

### Virtual Environments
- Create separate virtual environments for different sections when they have conflicting dependencies
- Document required Python version if specific version is needed
- Keep virtual environment directories (`venv/`, `env/`) in .gitignore

## Common Patterns

### Importing from Other Levels
When examples need to reference code from other sections:
```python
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "01-beginner"))
from module_name import function_name
```

### Data Files
- Store example data in `data/` subdirectories within each level
- Use small sample datasets in the repository
- Document where to download larger datasets (don't commit large files)

### Configuration
- Use environment variables for sensitive data (API keys, credentials)
- Consider `.env` files with python-dotenv for local configuration
- Provide `.env.example` templates without actual secrets

## Notes

- This is an educational repository - prioritize clarity and learning over production optimization
- Examples should be self-contained and runnable without complex setup
- Comments should explain *why* not just *what*
- Consider different skill levels when adding complexity
- Test examples to ensure they work on Windows (PowerShell environment)
