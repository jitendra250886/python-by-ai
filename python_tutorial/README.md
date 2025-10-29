
# 🐍 Python Tutorial (AI‑Assisted) — Index

> Goal: A **concise, practical roadmap** you can skim. Each module has small, runnable snippets. Use AI to summarize, explain errors, and propose alternatives — but keep **code minimal** and **tested locally**.

## 0. Start Here
- **Prereqs:** Python 3.11+, Git, VS Code/Visual Studio, basic terminal
- **Setup:** `python -m venv venv` → activate → `pip install -r requirements.txt` (add later)
- **How to use:** Read left → code right. Keep a `lab_notes.md` per session.

## 1. Python Basics
Variables & types, control flow, functions, modules, packages, I/O, errors, OOP basics.
**Libs:** built‑ins, `pathlib`, `argparse`, `logging`.

## 2. Data Handling & EDA
NumPy arrays, pandas DataFrames, data cleaning, joins, groupby, EDA.
**Libs:** `numpy`, `pandas`, `matplotlib`, `seaborn`, `jupyter`.

## 3. Files & OS
CSV/JSON/Excel, binary, compression, filesystem ops.
**Libs:** `csv`, `json`, `zipfile`, `shutil`, `pathlib`, `openpyxl`.

## 4. Web & APIs
HTTP, REST, auth, pagination, retries.
**Libs:** `requests`, `httpx`, `urllib`, `websockets`.

## 5. Web Scraping
Parsing, CSS/XPath, pagination, rendering, anti‑scraping basics.
**Libs:** `beautifulsoup4`, `lxml`, `scrapy`, `selenium`/`playwright`.

## 6. Databases
SQLite quick start, PostgreSQL, ORM patterns.
**Libs:** `sqlite3`, `psycopg`, `sqlalchemy`.

## 7. Automation & CLI
Arg parsing, logging, scheduling, subprocess.
**Libs:** `argparse`, `logging`, `schedule`, `subprocess`.

## 8. Images
Load, resize, crop, filters, OCR.
**Libs:** `Pillow`, `opencv-python`, `pytesseract`.

## 9. Audio
Load, trim, convert, features (MFCC), basic classification.
**Libs:** `pydub`, `librosa`, `soundfile`.

## 10. Video
Read/write, cut/concat, frames, simple effects.
**Libs:** `moviepy`, `opencv-python`, `ffmpeg-python`.

## 11. NLP
Tokenization, lemmatization, basic text classification, embeddings (intro).
**Libs:** `spaCy`, `nltk`, `scikit-learn`.

## 12. Machine Learning
Pipelines, train/test split, metrics, model save/load.
**Libs:** `scikit-learn`, `joblib`, `xgboost`.

## 13. Deep Learning (Intro)
Tensors, simple MLP/CNN, training loop basics.
**Libs:** `torch`/`tensorflow` (pick one), `torchvision`.

## 14. Visualization & Apps
Charts & dashboards; quick data apps.
**Libs:** `matplotlib`, `seaborn`, `plotly`, `streamlit`.

## 15. Fast APIs & Microservices
Build and test JSON APIs.
**Libs:** `fastapi`, `uvicorn`, `flask`, `requests` (testing).

## 16. Concurrency
`asyncio`, threads, processes; when to use which.

## 17. Testing & Quality
Unit tests, coverage, lint, format, types.
**Libs:** `pytest`, `coverage`, `flake8`, `black`, `mypy`.

## 18. Packaging & Environments
`pyproject.toml`, build & install, Poetry vs. pip, virtualenv vs. conda.

## 19. Deployment
Docker basics, env vars, logging, config.
**Libs:** `docker`, `gunicorn`, `uvicorn`.

## 20. Performance & Security (Essentials)
Profiling (`cProfile`), memory tips, `.env`/secrets, validation.
**Libs:** `pydantic`.

## 21. Patterns & Project Structure
SRC layout, config, Make/Tasks, reusable modules.

---
### 📂 Folder Plan (suggested)
```
python_tutorial/
  README.md                 # this index
  01_PYTHON_BASICS.md
  02_AI_TOOLS_SUMMARY.md
  modules/
    02_data_eda.md
    03_files_os.md
    04_web_apis.md
    05_web_scraping.md
    06_databases.md
    07_automation_cli.md
    08_images.md
    09_audio.md
    10_video.md
    11_nlp.md
    12_ml.md
    13_dl.md
    14_viz_apps.md
    15_fastapi_microservices.md
    16_concurrency.md
    17_testing_quality.md
    18_packaging_envs.md
    19_deployment.md
    20_perf_security.md
    21_patterns_structure.md
```

### 🔗 Navigation
- Next → **[01_PYTHON_BASICS.md](01_PYTHON_BASICS.md)**
- Tools Summary → **[02_AI_TOOLS_SUMMARY.md](02_AI_TOOLS_SUMMARY.md)**
- Modules → **`modules/`** (fill gradually; keep each file short!)
