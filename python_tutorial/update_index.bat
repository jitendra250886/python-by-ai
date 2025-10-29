@echo off
setlocal ENABLEDELAYEDEXPANSION

REM ==============================================
REM Documentation index generator
REM - Rebuilds INDEX.md in the current directory
REM - Rebuilds FULL_COURSE_INDEX.md with recursive listing
REM - Rebuilds per-folder INDEX.md files for all subdirectories
REM ==============================================

REM ---- Root INDEX.md (current folder only)
(
  echo # Documentation Index
  echo.
  echo Below is an auto-generated list of Markdown files in this folder:
  echo.
  for /f "delims=" %%f in ('dir /b /on *.md 2^>nul') do (
    if /i not "%%f"=="INDEX.md" if /i not "%%f"=="FULL_COURSE_INDEX.md" echo - [%%f](%%f)
  )
) > INDEX.md

REM ---- FULL_COURSE_INDEX.md (recursive)
(
  echo # Full Course Index
  echo.
  echo Hierarchical list of all Markdown files under this folder (auto-generated).
  echo.
  for /r %%F in (*.md) do (
    set "abs=%%F"
    set "rel=!abs:%CD%\=!."
    for %%# in (!rel!) do set "name=%%~nx#"
    if /i not "!name!"=="INDEX.md" if /i not "!name!"=="FULL_COURSE_INDEX.md" echo - [!rel!](./!rel!)
  )
) > FULL_COURSE_INDEX.md

REM ---- Per-folder INDEX.md files
for /f "delims=" %%D in ('dir /b /ad /s 2^>nul') do (
  pushd "%%D" >nul 2>&1
  (
    echo # Documentation Index
    echo.
    echo Below is an auto-generated list of Markdown files in this folder:
    echo.
    for /f "delims=" %%f in ('dir /b /on *.md 2^>nul') do (
      if /i not "%%f"=="INDEX.md" if /i not "%%f"=="FULL_COURSE_INDEX.md" echo - [%%f](%%f)
    )
  ) > INDEX.md
  popd >nul 2>&1
)

echo Index files regenerated: INDEX.md (root), FULL_COURSE_INDEX.md, and per-folder INDEX.md files.