# Python Cheat Sheet (concise)

## Install & Verify
- Download from https://www.python.org/downloads/
- During install on Windows: **check "Add Python to PATH"**.
```bash
python --version
pip --version
```

## Virtual Environment (recommended per project)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
# leave venv
deactivate
```

## Packages
```bash
pip install <pkg>
pip uninstall <pkg>
pip list
pip freeze > requirements.txt        # save current env
pip install -r requirements.txt      # recreate env
```

## Run Code
```bash
python hello.py
python -m <module>                   # run as module
```

## Useful Snippets
```python
# argparse (CLI)
import argparse
p = argparse.ArgumentParser()
p.add_argument('--name', default='World')
args = p.parse_args()
print(f"Hello, {args.name}!")

# env vars
import os
API_KEY = os.getenv('API_KEY')

# file I/O
with open('data.txt','w') as f:
    f.write('hello')
with open('data.txt') as f:
    print(f.read())
```

## Testing & Quality
```bash
python -m unittest -v          # run tests
pip install flake8 black mypy  # install tools
flake8 .                       # lint
black .                        # format
mypy .                         # type-check
```

## Common Pitfalls
- Activate the **venv** before installing/running.
- If `python` not found on Windows, try `py -3 --version` or reinstall with PATH.

---
[⬅ Back to Cheat Sheet Index](CHEATSHEET_INDEX.md)

