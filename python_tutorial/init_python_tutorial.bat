
@echo off
REM Create python_tutorial structure and starter files (if not exist)
set ROOT=python_tutorial
if not exist %ROOT% mkdir %ROOT%
if not exist %ROOT%\modules mkdir %ROOT%\modules

REM Write README.md (index)
powershell -NoProfile -Command ^
  "$md=@'
# 🐍 Python Tutorial (AI‑Assisted) — Index
(…shortened; use the version from the ZIP README.md you downloaded…)
'@; $md | Out-File -Encoding utf8 %ROOT%\README.md"

echo # Coming soon> %ROOT%\modules\02_data_eda.md

REM Add more echo/PowerShell blocks as needed for other files

echo Done. Open %ROOT%\README.md
