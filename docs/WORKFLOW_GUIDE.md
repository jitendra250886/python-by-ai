# One-Page Python Project Workflow

## 1. Clone Repo
```bash
git clone <repo-url>
cd <repo>
```

## 2. Create Virtual Environment
```bash
python -m venv venv
# Activate
venv\Scripts\activate    # Windows
source venv/bin/activate # macOS/Linux
```

## 3. Install Dependencies
```bash
pip install -r requirements.txt   # if file exists
```

## 4. Run Code
```bash
python hello.py
```

## 5. Format & Lint
```bash
black .      # format code
flake8 .     # lint
mypy .       # type-check
```

## 6. Test
```bash
python -m unittest -v
```

## 7. Commit & Push
```bash
git status
git add .
git commit -m "feat: add new feature"
git push
```

## 8. Pull Request (GitHub)
- Push feature branch.
- Open PR → review → merge.

---
**Tip:** Repeat steps 4–7 for each change. Keep commits small and meaningful.


---
[⬅ Back to Cheat Sheet Index](CHEATSHEET_INDEX.md)

