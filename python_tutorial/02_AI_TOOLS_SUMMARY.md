
# 02 — AI‑Assisted Tools & Prompts (summary)

> Use AI for speed, not as a source of truth. Keep code **minimal**, **runnable**, **locally verified**.

## 1) What AI is great for
- Summaries of docs/code; quick comparisons of approaches.
- Explaining errors / stack traces and proposing minimal fixes.
- Generating **skeletons** (CLI, tests, classes) you will refine.
- Prompting alternative solutions (performance, readability).

## 2) Prompt patterns (copy & adapt)
- **Explain error**: "Explain this traceback and show a minimal fix: ```<trace>```"
- **Refactor**: "Refactor this function for readability; keep outputs identical. ```<code>```"
- **Design**: "Sketch a clean folder structure for a small FastAPI + pandas app."
- **Tests**: "Write 5 pytest cases for this function (include edge cases). ```<code>```"
- **Docs**: "Summarize this module in 5 bullets with a 10‑line usage example."
- **Perf**: "Profile hints: where could this be O(n^2)? suggest O(n log n)."

## 3) Verification workflow (always)
1. Ask for **minimal reproducible example** (≤ 20 lines).
2. Run locally; confirm it works.
3. Add/adjust tests; re‑run.
4. Only then integrate into your project.

## 4) Privacy & Safety
- Never paste **secrets**, API keys, or proprietary data.
- Redact/obfuscate inputs; use small synthetic samples.
- Keep `.env` out of prompts and under `.gitignore`.

## 5) Tooling short list
- Quality: `pytest`, `coverage`, `flake8`, `black`, `mypy`
- Data/EDA: `numpy`, `pandas`, `matplotlib`, `seaborn`
- Web/API: `requests`, `httpx`, `fastapi`, `flask`
- Scraping: `beautifulsoup4`, `lxml`, `scrapy`, `playwright`
- Media: `opencv-python`, `Pillow`, `librosa`, `moviepy`
- ML/DL: `scikit-learn`, `xgboost`, `torch`/`tensorflow`

## 6) Example AI session
```
Goal: Read CSV → clean → simple chart.
Prompt: "Give a 30‑line script using pandas to read data.csv, drop NA, parse dates, plot a line, save plot.png. Include imports; no extras."
Check: Run; if errors, paste trace and ask: "Fix only the failing line; keep total lines ≤ 30."
```

## 7) Red flags
- Huge replies; missing imports; code that cannot run.
- Complex setup to achieve simple tasks — ask for **simpler**.

## 8) Keep a change log
- `CHANGELOG.md`: bullets of what changed and why.
- Commit small; one topic per commit.

---
[⬅ Back to Index](README.md)
