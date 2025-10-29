
# CMD Windows Cheat Sheet (concise, one-liners)

> Use in **Command Prompt (cmd.exe)**. Many commands need an **elevated** (Run as administrator) prompt.

---
## Navigation & Listing
```cmd
cd path                 :: change directory
cd ..                   :: up one level
cd /d D:\projects       :: change drive & dir
pushd \\server\share     :: map & change to network path; use popd to return
popd                    :: return to previous dir
pwd                     :: (cmd has no pwd) use: echo %cd%

dir                      :: list files
 dir /b                 :: bare names only
 dir /s /b              :: recursive bare list (full paths)
 dir /od /t:w           :: sort by modified time
```

## Files & Folders
```cmd
mkdir folder            :: create folder(s)
mkdir a\b\c            :: create nested
rmdir folder            :: remove empty folder
rmdir /s /q folder      :: remove folder tree (quiet)

del file.txt            :: delete file
 del /q /f /s *.tmp     :: quiet, force, recurse
copy src dst            :: copy file
copy /y src dst         :: suppress overwrite prompt
xcopy src dst /e /i /y  :: copy dirs; /e empty dirs; /i assume dir
robocopy src dst /e     :: robust copy (recommended for dirs)
move src dst            :: move/rename
ren old new             :: rename
attrib +h -r file       :: set hidden, remove read-only
fc file1 file2          :: compare files
```

## View & Search Content
```cmd
type file.txt           :: print file
more file.txt           :: page output
find "text" file.txt     :: simple search (case-sensitive)
find /i /n "text" file  :: case-insensitive, show line numbers
findstr /s /i /n pattern *.log :: recursive search, ignore case
findstr /r ".*error.*" *.txt  :: regex search
where /r . *.dll        :: locate files by name, recursively
forfiles /S /M *.log /D -7 /C "cmd /c del @file" :: delete .log older than 7 days
```

## System Info & Admin
```cmd
whoami /user            :: current user SID
whoami /groups          :: group membership
hostname                :: computer name
systeminfo              :: system details
ver                     :: Windows version
wmic cpu get name       :: CPU info (legacy but handy)
set                     :: list env vars
setx NAME value         :: set user env var (persist)
setx PATH "%PATH%;C:\tools" :: append folder to PATH (new sessions)
```

## Users & Groups (admin)
```cmd
net user                :: list users
net user alice P@ss! /add       :: add user
net localgroup          :: list groups
net localgroup Administrators alice /add :: add user to admins
net user alice /active:no        :: disable user
```

## Processes & Services
```cmd
tasklist                        :: list processes
tasklist /fi "imagename eq notepad.exe" :: filter by name
taskkill /im notepad.exe /f     :: kill by name (force)
taskkill /pid 1234 /f           :: kill by PID
sc query type= service state= all :: list services
sc start Spooler                :: start service
sc stop Spooler                 :: stop service
```

## Networking
```cmd
ipconfig /all                   :: full IP config
ping -n 5 example.com           :: 5 echo requests
tracert example.com             :: route trace
nslookup example.com            :: DNS lookup
netstat -ano                    :: ports, PIDs
arp -a                          :: ARP table
route print                     :: routing table
netsh wlan show profiles        :: saved Wi‑Fi profiles
```

## Disks & Filesystems
```cmd
df                              :: (no df in cmd) use: wmic logicaldisk get size,freespace,caption
chkdsk C:                       :: check disk
sfc /scannow                    :: system file check (admin)
DISM /Online /Cleanup-Image /RestoreHealth :: repair image (admin)
compact /c /s:C:\data          :: NTFS compress folder
```

## Compression & Archives (Windows 10+)
```cmd
tar -czvf out.tgz folder        :: create gzip tar
tar -xzvf out.tgz               :: extract
powershell -c "Compress-Archive file out.zip"    :: zip via PowerShell
powershell -c "Expand-Archive out.zip -DestinationPath ." :: unzip
```

## Scheduling & Automation
```cmd
schtasks /query                 :: list tasks
schtasks /create /sc daily /tn "Backup" /tr "C:\scripts\backup.bat" /st 23:00 :: daily task 11 PM
```

---
# Batch Files (.bat) — quick guide

## Create & Run
1) Open Notepad → paste lines → save as `script.bat` (encoding ANSI/UTF‑8, **Save as type: All Files**).
2) Run by double‑click or from cmd: `script.bat` (ensure folder is in PATH or call with full path).

## Basics
```bat
@echo off                 
REM comments start with REM
set NAME=Jitendra         
echo Hello %NAME%         
exit /b 0                 :: set exit code 0
```

## Arguments & Error Handling
```bat
@echo off
REM args: %1 %2 ...
echo first arg: %1
REM run a command and check errorlevel
somecmd.exe
if errorlevel 1 (
  echo Failed with code %errorlevel%
  exit /b %errorlevel%
)
```

## Loops & Conditionals
```bat
for %%f in (*.txt) do echo %%f           :: iterate files
for /f "tokens=1,2 delims=," %%a in (list.csv) do echo %%a %%b :: parse CSV
if exist config.ini echo found config    :: file existence
if "%1"=="build" echo Building...       :: compare strings
```

## Call other scripts & return codes
```bat
call setup.bat          :: run and return
call :step1             :: call label
rem ...
exit /b 0
:step1
echo Step1
exit /b 0
```

## Common automation examples
```bat
@echo off
REM Git one‑shot commit
pushd C:\projects\Python-by-AI
call venv\Scripts\activate 2>nul
git status
git add .
git commit -m "chore: update docs"
git push
popd
```

```bat
@echo off
REM Rotate logs older than 7 days
forfiles /S /M *.log /D -7 /C "cmd /c del @file"
```

## Run as Administrator
- Right‑click **cmd.exe** → Run as administrator, or create a shortcut set to **Run as administrator**.
- Some commands (net user, sc, sfc, DISM) require elevation.

## Make scripts runnable from anywhere
```cmd
setx PATH "%PATH%;C:\scripts"   :: add folder to PATH (new sessions)
```

---
# Minimum changes to add this sheet to your docs
- In `docs/CHEATSHEET_INDEX.md`, add:
```markdown
### 🔗 [CMD_WINDOWS_CHEATSHEET.md](CMD_WINDOWS_CHEATSHEET.md)
**Why essential:** Core CMD commands, batch scripting basics, and automation tips for Windows.
```
- (Optional) Add a link in `docs/README.md` under your reference list.

## Git: stage, commit, push
```bash
git add docs/CMD_WINDOWS_CHEATSHEET.md docs/CHEATSHEET_INDEX.md
git commit -m "docs: add CMD Windows cheat sheet and index link"
git push
```

---
[⬅ Back to Cheat Sheet Index](CHEATSHEET_INDEX.md)
