# 04 — Web Scraping with Python (Ethical & Robust)

> A pragmatic guide to fetching, parsing, and extracting data from the web **responsibly**.

> ⚠️ **Legal & ethical notice**: Always review a site's **Terms of Service**, check `robots.txt`, avoid personal data, rate‑limit your requests, and never disrupt a site. Scrape only what you are permitted to, for legitimate purposes.

---

## Learning objectives
- Understand the request–response model, headers, and robots rules.
- Fetch pages reliably (retries, timeouts, backoff) and **identify** yourself.
- Parse HTML with **BeautifulSoup** (or `lxml`) and CSS selectors.
- Handle pagination, sitemaps, and table extraction.
- Store clean data into CSV/JSON, with basic validation.

---

## 1) Inspect before you scrape
1. Visit the site in your browser.
2. Open Developer Tools → **Network** + **Elements** tabs.
3. Identify the **URL(s)** actually returning data (often JSON APIs!).
4. Prefer official exports/APIs when available.

---

## 2) Respect `robots.txt`
```python
import urllib.robotparser as rp

rp = rp.RobotFileParser()
rp.set_url('https://example.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'https://example.com/public/page'))
```
> Robots are advisory, not law; always check Terms of Service.

---

## 3) Fetching pages (with retries & headers)
```python
import time
import random
import urllib.request
from urllib.error import URLError, HTTPError

HEADERS = {"User-Agent": "YourProjectBot/1.0 (+contact@example.com)"}

def fetch(url, retries=3, backoff=1.5, timeout=15):
    req = urllib.request.Request(url, headers=HEADERS)
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode('utf-8', errors='replace')
        except (HTTPError, URLError) as e:
            if attempt == retries:
                raise
            sleep_for = backoff ** attempt + random.uniform(0, 0.5)
            time.sleep(sleep_for)

html = fetch('https://quotes.toscrape.com/')
print(html[:400])
```

> You can also use `requests` for a simpler API (`pip install requests`).

---

## 4) Parse HTML with BeautifulSoup
> Install: `pip install beautifulsoup4 lxml`
```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
quotes = []
for q in soup.select('div.quote'):
    text = q.select_one('span.text').get_text(strip=True)
    author = q.select_one('small.author').get_text(strip=True)
    tags = [t.get_text(strip=True) for t in q.select('div.tags a.tag')]
    quotes.append({"text": text, "author": author, "tags": tags})

print(quotes[:2])
```

---

## 5) Pagination
```python
import urllib.parse

base = 'https://quotes.toscrape.com'
url = base
all_quotes = []

while url:
    html = fetch(url)
    soup = BeautifulSoup(html, 'lxml')
    for q in soup.select('div.quote'):
        all_quotes.append(q.select_one('span.text').get_text(strip=True))
    next_link = soup.select_one('li.next > a')
    url = urllib.parse.urljoin(base, next_link['href']) if next_link else None

print('Collected', len(all_quotes), 'quotes')
```

---

## 6) Extracting tables quickly (when allowed)
```python
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
# pd.read_html uses lxml under the hood
dfs = pd.read_html(url)  # returns list of tables
print('Found tables:', len(dfs))
print(dfs[0].head())
```

---

## 7) Save as CSV/JSON with validation
```python
import csv, json
from pathlib import Path

def validate(q):
    return isinstance(q.get('text'), str) and q.get('text')

valid = [q for q in quotes if validate(q)]

# JSON
Path('quotes.json').write_text(json.dumps(valid, ensure_ascii=False, indent=2), encoding='utf-8')

# CSV (flatten tags)
with Path('quotes.csv').open('w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['text', 'author', 'tags'])
    w.writeheader()
    for q in valid:
        w.writerow({**q, 'tags': '|'.join(q['tags'])})
```

---

## 8) Handling dynamic sites
Some pages render content via JavaScript after load. Options:
- Look for the underlying **JSON API** the page calls (best choice).
- Use **Selenium** or **Playwright** to drive a headless browser.
- Use **network inspection** to emulate the minimal web requests.

> Selenium snippet (requires install & driver):
```python
# pip install selenium webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get('https://example.com')
    html = driver.page_source
finally:
    driver.quit()
```

---

## 9) Be nice: throttling & caching
- Add **delays** between requests; randomize slightly.
- Limit concurrency; avoid hammering a site.
- Cache responses with `requests-cache` for repeat runs.
- Rotate IPs/headers only if permitted and necessary.

---

## 10) Common pitfalls checklist
- ❌ Ignoring Terms/robots and hammering the site.
- ❌ Parsing by brittle string splits instead of DOM selectors.
- ❌ No retries/timeouts → flaky scripts.
- ❌ Dumping raw data without validation/normalization.
- ❌ Forgetting to identify your client (User-Agent).

---

## 11) Mini‑exercises
1. Scrape all quotes and authors from `https://quotes.toscrape.com/` into `quotes.json`.
2. Crawl a small blog, follow pagination, and export post titles and URLs to CSV.
3. Use `rp.can_fetch` to skip disallowed paths during a crawl.
4. Try `pandas.read_html` on a government open‑data page (where allowed) and save the first table to Excel.

---

### Further reading
- Libraries: `beautifulsoup4`, `lxml`, `requests`, `selenium`, `pandas`.
- Topics: HTTP caching, robots and sitemaps, structured data (`schema.org`).