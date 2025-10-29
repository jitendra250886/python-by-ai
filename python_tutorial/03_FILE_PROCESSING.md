# 03 — File Processing in Python

> Learn practical, **safe**, and **scalable** ways to work with files and folders in Python using the standard library and a few well‑known tools.

---

## Learning objectives
By the end of this module, you will be able to:
- Work with **paths** and the filesystem using `pathlib` and `os`.
- **Read** and **write** text, binary, CSV, JSON, and compressed files.
- Traverse directories safely and handle **large files** efficiently.
- Use **context managers**, **error handling**, and **temporary files**.
- Apply best practices for **encoding**, **robustness**, and **performance**.

> 🧰 Prerequisites: Python 3.9+, basic understanding of exceptions and data types.

---

## 1) Paths & filesystem basics

### Use `pathlib` (recommended)
```python
from pathlib import Path

# Current working directory
cwd = Path.cwd()
print(cwd)

# Build paths safely (avoids manual string concat)
data_dir = cwd / "data" / "inputs"

# Ensure a directory exists
(data_dir).mkdir(parents=True, exist_ok=True)

# Check existence & type
p = data_dir / "sample.txt"
print(p.exists(), p.is_file(), p.is_dir())

# Iterate files
for f in data_dir.glob('**/*.txt'):
    print(f.name, f.stat().st_size, 'bytes')
```

### When you must use `os`
```python
import os
print(os.getcwd())
print(os.listdir('.'))
```

> ✅ Tip: Prefer `pathlib` for readability, immutability, and method discoverability.

---

## 2) Reading & writing text files

### Always use a context manager
```python
from pathlib import Path
p = Path('notes.txt')

# Write text
with p.open('w', encoding='utf-8', newline='') as f:
    f.write('Hello, world!\n')
    f.writelines(['Line 2\n', 'Line 3\n'])

# Read all
with p.open('r', encoding='utf-8') as f:
    content = f.read()
    print(content)

# Read line-by-line (memory efficient)
with p.open('r', encoding='utf-8') as f:
    for line in f:
        print(line.rstrip())
```

### Encodings & newlines
- Use `encoding='utf-8'` almost always.
- Use `errors='replace'` or `errors='ignore'` if you must deal with messy input.
- Use `newline=''` when writing CSV to avoid extra blank lines on Windows.

---

## 3) Binary files (images, PDFs, etc.)
```python
from pathlib import Path
src = Path('image.jpg')
dst = Path('copy.jpg')

# Copy binary bytes manually (simple)
with src.open('rb') as r, dst.open('wb') as w:
    while True:
        chunk = r.read(1024 * 1024)  # 1 MB
        if not chunk:
            break
        w.write(chunk)
```

---

## 4) CSV, JSON, and Excel basics

### CSV (standard library)
```python
import csv
from pathlib import Path

rows = [
    {"id": 1, "name": "Alice", "score": 88.5},
    {"id": 2, "name": "Bob",   "score": 92.0},
]

# Write
with Path('scores.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

# Read
with Path('scores.csv').open('r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)
    print(data)
```

### JSON
```python
import json
from pathlib import Path

config = {"version": 1, "features": ["auth", "export"], "debug": False}
Path('config.json').write_text(json.dumps(config, indent=2), encoding='utf-8')

loaded = json.loads(Path('config.json').read_text(encoding='utf-8'))
print(loaded["features"][0])
```

### Excel (using `pandas`, optional)
> Requires `pandas` and `openpyxl` installed.
```python
import pandas as pd

df = pd.DataFrame(rows)
# Write .xlsx
with pd.ExcelWriter('scores.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Scores', index=False)
# Read .xlsx
back = pd.read_excel('scores.xlsx', sheet_name='Scores', engine='openpyxl')
print(back.head())
```

---

## 5) Directory traversal & patterns
```python
from pathlib import Path

root = Path('logs')
for path in root.rglob('*.log'):
    size = path.stat().st_size
    if size > 10_000:
        print('Large log:', path, size)
```

Use `glob()` for shallow searches and `rglob()` for recursive ones.

---

## 6) Large files: stream in chunks
```python
from pathlib import Path

size = 0
with Path('bigfile.dat').open('rb') as f:
    while chunk := f.read(4 * 1024 * 1024):  # 4 MB
        size += len(chunk)
print('Total bytes:', size)
```

---

## 7) Compression: ZIP, GZIP, TAR
```python
import gzip, tarfile, zipfile
from pathlib import Path

# GZIP single file
with open('data.txt', 'rb') as src, gzip.open('data.txt.gz', 'wb') as dst:
    dst.writelines(src)

# ZIP multiple files
with zipfile.ZipFile('archive.zip', 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for p in Path('data').rglob('*'):
        if p.is_file():
            z.write(p, arcname=p.relative_to('data'))

# TAR (optionally gzip/zip)
with tarfile.open('bundle.tar.gz', 'w:gz') as tar:
    tar.add('data', arcname='data')
```

---

## 8) Temporary files & directories
```python
i mport tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmpdir:
    tmp = Path(tmpdir) / 'scratch.txt'
    tmp.write_text('hello', encoding='utf-8')
    print('Created at', tmp)
# auto-cleaned
```

---

## 9) File metadata & times
```python
from pathlib import Path
import time

p = Path('notes.txt')
st = p.stat()
print('Size:', st.st_size)
print('Modified:', time.ctime(st.st_mtime))
```

---

## 10) Error handling patterns
```python
from pathlib import Path

try:
    data = Path('maybe.txt').read_text(encoding='utf-8')
except FileNotFoundError:
    print('File not found')
except PermissionError:
    print('No permissions')
else:
    print('Loaded OK')
finally:
    print('Done')
```

---

## 11) Best practices checklist
- ✅ Prefer `pathlib` over string paths.
- ✅ Always use **context managers** (`with ...`) for file I/O.
- ✅ Default to `encoding='utf-8'`.
- ✅ Stream large files in **chunks**.
- ✅ Validate inputs; handle **exceptions** explicitly.
- ✅ Use `tempfile` for scratch work; clean up after yourself.
- ✅ Keep I/O off the main thread in UI apps / services.
- ✅ Log file operations for auditability in production.

---

## 12) Mini‑exercises
1. Write a script that merges all `.csv` files in a folder into `all.csv` (include headers only once).
2. Walk a directory tree and print the 10 largest files.
3. Convert a folder of `.txt` files into a single `.zip` with relative paths preserved.
4. Parse `config.json` and fail fast with a helpful message if required keys are missing.

---

### Further reading
- Python docs: `pathlib`, `io`, `csv`, `json`, `tempfile`, `zipfile`, `gzip`, `tarfile`.