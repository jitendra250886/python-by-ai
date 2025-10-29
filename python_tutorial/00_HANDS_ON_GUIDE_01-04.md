# Hands‑On Guide — Modules 01–04

A consolidated, lab‑driven companion for the first four modules. Each lab is designed to be copy‑paste runnable and to reinforce practical skills.

> **How to use**: Pick a lab, create a fresh folder, and follow the tasks. Save your answers in a `solutions/` subfolder.

---

## Module 01 — Environment & Python Basics *(starter labs)*
> If your Module 01 material is elsewhere, you can still use these labs as a quick on‑ramp.

### Lab 1.1 — Set up your workspace
- Create a virtual environment (`python -m venv .venv`) and activate it.
- Create a file `hello.py` that prints `Hello, <your name>`.
- Add a `.gitignore` and ignore `.venv/` and `__pycache__/`.

### Lab 1.2 — CLI arguments & stdout
Create `greeter.py` that reads a name from CLI args and prints `Hi, <name>!`.

```python
# greeter.py
import sys
name = sys.argv[1] if len(sys.argv) > 1 else 'there'
print(f"Hi, {name}!")
```

**Stretch**: Add `--upper` flag to shout the greeting.

---

## Module 02 — Data Structures & Control Flow *(practice set)*

### Lab 2.1 — Top‑N frequencies
Read a list of words and print the top‑3 most common.
```python
from collections import Counter
words = "the quick brown fox jumps over the lazy dog the fox was quick".split()
print(Counter(words).most_common(3))
```

### Lab 2.2 — Small utilities
- Write `dedupe(seq)` that preserves order.
- Write `chunk(seq, n)` to yield chunks of size `n`.
- Test with lists of ints and strings.

---

## Module 03 — File Processing *(hands‑on)*
See: [03_FILE_PROCESSING.md](03_FILE_PROCESSING.md)

### Lab 3.1 — Merge CSVs safely
**Goal**: Merge all `.csv` files in `data/` to `merged.csv`, writing headers once and normalizing field order.

**Steps**
1. Detect all `*.csv` in `data/` (non‑recursive).
2. Infer the union of all headers and use a consistent order.
3. Write `merged.csv` with UTF‑8 encoding.

**Starter**
```python
import csv
from pathlib import Path

src_dir = Path('data')
files = sorted(src_dir.glob('*.csv'))
headers = []
for f in files:
    with f.open('r', encoding='utf-8', newline='') as fh:
        r = csv.DictReader(fh)
        headers.extend(h for h in r.fieldnames if h not in headers)

with Path('merged.csv').open('w', encoding='utf-8', newline='') as out:
    w = csv.DictWriter(out, fieldnames=headers)
    w.writeheader()
    for f in files:
        with f.open('r', encoding='utf-8', newline='') as fh:
            for row in csv.DictReader(fh):
                w.writerow({h: row.get(h, '') for h in headers})
```

### Lab 3.2 — Compress & checksum
Zip the `artifacts/` folder to `artifacts.zip` and compute its size and SHA‑256.

```python
import hashlib, zipfile
from pathlib import Path

with zipfile.ZipFile('artifacts.zip', 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for p in Path('artifacts').rglob('*'):
        if p.is_file():
            z.write(p, p.relative_to('artifacts'))

h = hashlib.sha256()
with open('artifacts.zip','rb') as f:
    for chunk in iter(lambda: f.read(1<<20), b''):
        h.update(chunk)
print('sha256:', h.hexdigest())
```

---

## Module 04 — Web Scraping *(hands‑on)*
See: [04_WEB_SCRAPING.md](04_WEB_SCRAPING.md)

### Lab 4.1 — Quotes to CSV
Scrape quote text, author, and tags from the first page of `https://quotes.toscrape.com/` into `quotes.csv` (respectful fetching, custom UA, timeouts, retries).

### Lab 4.2 — Pagination walker
Follow the `Next` link across all pages and save to `quotes.json`. Validate each object has `text` and `author`.

### Lab 4.3 — Table extraction
Use `pandas.read_html` on a permitted page and export the first table to `table.xlsx`.

---

## Rubric (self‑check)
- ✅ Uses `pathlib`, context managers, and UTF‑8 by default.
- ✅ Includes timeouts/retries and a descriptive User‑Agent for web requests.
- ✅ Streams large I/O in chunks; avoids loading entire files when unnecessary.
- ✅ Saves clean, validated CSV/JSON; includes basic logging/printouts.

---

## Challenge Project — Mini data pipeline
1. Download a small web table (allowed page) with `pandas.read_html`.
2. Normalize column names (lowercase, snake_case).
3. Save CSV, Excel, and a compressed ZIP.
4. Generate a `REPORT.md` summarizing row counts and file sizes.