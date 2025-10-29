# VS Code Cheat Sheet (Python Development)

## Install & Setup
- Download: https://code.visualstudio.com/
- Extensions:
  - **Python** (Microsoft)
  - **Pylance** (IntelliSense)
  - **Jupyter** (optional)
  - **Markdown All in One**

## Open Project
- **File → Open Folder** → select repo folder.
- Integrated Terminal: `Ctrl+`` (backtick).

## Run Python
- Open `.py` file → click **Run Python File** in top-right OR:
```bash
python <file>.py
```

## Debugging
- Set breakpoint (click gutter).
- **F5** Start Debug.
- **Shift+F5** Stop.
- **F10** Step Over, **F11** Step Into.

## Virtual Environment
- Create venv:
```bash
python -m venv venv
```
- Activate in terminal:
```bash
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
- Select interpreter: **Ctrl+Shift+P → Python: Select Interpreter → choose venv**.

## Git Integration
- **Source Control** panel: stage, commit, push.
- **Ctrl+Shift+G** opens Source Control.

## Useful Shortcuts
```
Ctrl+Shift+P   Command Palette
Ctrl+`         Toggle Terminal
Ctrl+P         Quick Open
Ctrl+B         Toggle Sidebar
Ctrl+F / Ctrl+H Find / Replace
Ctrl+/          Toggle Line Comment
Shift+Alt+A     Block Comment
Shift+Alt+F     Format Document
F5 / Ctrl+F5    Debug / Run without Debug
Ctrl+K Ctrl+S   Keyboard Shortcuts
Ctrl+Shift+V    Markdown Preview
```

## Tips
- Use **settings.json** for custom configs.
- Enable **auto-save** for convenience.
- Use **workspace settings** for project-specific interpreter.


---
[⬅ Back to Cheat Sheet Index](CHEATSHEET_INDEX.md)

