
# 01 — Python Basics (quick, runnable)

> Keep it tiny. Copy → run. Expand only when needed.

## 0) Setup
```bash
python --version
python -m venv venv
# Windows:  venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install --upgrade pip
```

## 1) Hello & Types
```python
print("Hello, Python!")

x = 10          # int
pi = 3.14       # float
name = "Jitendra"  # str
ok = True       # bool
print(type(x), type(pi), type(name), type(ok))
```

## 2) Numbers & Strings
```python
print(5 // 2, 5 % 2, 2 ** 5)      # 2 1 32
s = "python"; print(s.upper(), s[:3], s[::-1])
print(f"Hi {name}, x+pi={x+pi}")
```

## 3) Lists / Tuples / Sets / Dicts
```python
nums = [1, 2, 3]; nums.append(4)
coords = (10, 20)
unique = {1, 1, 2}
user = {"name": "Jitendra", "role": "learner"}
print(nums, coords, unique, user["name"])  # [1,2,3,4] (10,20) {1,2} Jitendra
```

## 4) Control Flow
```python
n = 7
if n % 2 == 0:
    print("even")
elif n % 3 == 0:
    print("div by 3")
else:
    print("odd")
```

## 5) Loops & Comprehensions
```python
for i in range(3):
    print(i)

j = 3
while j:
    print(j); j -= 1

squares = [i*i for i in range(5)]
print(squares)
```

## 6) Functions
```python
def add(a: int, b: int = 0) -> int:
    return a + b
print(add(2, 3))
```

## 7) Modules & Packages
```python
# math_utils.py
# def square(x): return x*x
from math import sqrt
from math_utils import square  # ensure file exists
print(square(5), sqrt(16))
```

## 8) File I/O (Pathlib)
```python
from pathlib import Path
p = Path("data.txt")
p.write_text("hello")
print(p.read_text())
```

## 9) Exceptions & Logging
```python
import logging
logging.basicConfig(level=logging.INFO)
try:
    int("x")
except ValueError as e:
    logging.exception("Conversion failed: %s", e)
```

## 10) CLI with argparse (runnable)
```python
# app.py
import argparse
p = argparse.ArgumentParser()
p.add_argument('--name', default='World')
args = p.parse_args()
print(f"Hello, {args.name}!")
```
Run:
```bash
python app.py --name Jitendra
```

## 11) Simple Tests (pytest style)
```python
# test_add.py
from main import add

def test_add():
    assert add(2, 3) == 5
```
Run:
```bash
pip install pytest
pytest -q
```

## 12) Basic OOP
```python
class Counter:
    def __init__(self, start=0):
        self.value = start
    def inc(self):
        self.value += 1

c = Counter(); c.inc(); print(c.value)  # 1
```

## 13) Next
- Learn **pandas** & **matplotlib** for EDA.
- Try **requests** to call a JSON API.
- Add **flake8**, **black**, **mypy** for quality.

---
[⬅ Back to Index](README.md)
