# Quick Reference - Python Master Course

## 🚀 Quick Start Commands

### Launch Course
```bash
# Interactive menu (easiest)
python project_scripts/start_course.py

# Direct launch beginner course
jupyter notebook 01-beginner/

# Open specific lesson
jupyter notebook 01-beginner/01_introduction_to_python.ipynb
```

---

## 📂 Project Management

### View Project Structure
```bash
python project_scripts/generate_directory_structure.py
```

### Regenerate Course Notebooks
```bash
# Beginner course
python project_scripts/generate_beginner_notebooks.py
```

---

## 📚 Course Structure

### Beginner Course (01-beginner/) - 20 Lessons

**Module 1: Getting Started (1-3)**
- 01 - Introduction to Python ✅ Full content
- 02 - Variables and Data Types ✅ Full content
- 03 - Basic Operators ✅ Full content

**Module 2: Control Flow (4-6)**
- 04 - Conditional Statements 📝 Template
- 05 - For Loops 📝 Template
- 06 - While Loops 📝 Template

**Module 3: Data Structures (7-10)**
- 07 - Lists 📝 Template
- 08 - Tuples 📝 Template
- 09 - Dictionaries 📝 Template
- 10 - Sets 📝 Template

**Module 4: Functions (11-13)**
- 11 - Functions Basics 📝 Template
- 12 - Function Scope 📝 Template
- 13 - Advanced Functions 📝 Template

**Module 5: Strings & Files (14-16)**
- 14 - String Manipulation 📝 Template
- 15 - File Handling 📝 Template
- 16 - Error Handling 📝 Template

**Module 6: OOP Intro (17-18)**
- 17 - Classes and Objects 📝 Template
- 18 - OOP Fundamentals 📝 Template

**Module 7: Practice (19-20)**
- 19 - Coding Exercises 📝 Template
- 20 - Beginner Projects 📝 Template

---

## 🎓 For Web Platform

### Convert to Markdown
```bash
# Single file
jupyter nbconvert --to markdown 01-beginner/01_introduction_to_python.ipynb

# All beginner notebooks
jupyter nbconvert --to markdown 01-beginner/*.ipynb

# With output
jupyter nbconvert --to markdown --execute 01-beginner/01_introduction_to_python.ipynb
```

### Convert to HTML
```bash
jupyter nbconvert --to html 01-beginner/01_introduction_to_python.ipynb
```

---

## 🛠️ Development Workflow

### Adding Content to Lessons

1. **Edit generator script:**
   ```bash
   # Open in your editor
   code project_scripts/generate_beginner_notebooks.py
   ```

2. **Add content to LESSONS dictionary** (around line 62)

3. **Regenerate notebooks:**
   ```bash
   python project_scripts/generate_beginner_notebooks.py
   ```

4. **Test in Jupyter:**
   ```bash
   jupyter notebook 01-beginner/
   ```

### When Structure Changes

1. Update `generate_beginner_notebooks.py`
2. Update `01-beginner/INDEX.md`
3. Regenerate notebooks
4. Update `generate_directory_structure.py` if needed
5. Test everything

---

## 📁 File Locations

- **Beginner Index:** `01-beginner/INDEX.md`
- **Main README:** `README.md`
- **Setup Summary:** `SETUP_COMPLETE.md`
- **This File:** `QUICK_REFERENCE.md`

---

## 🎯 Next Steps

1. **Expand Lessons 4-20** - Add full content to remaining lessons
2. **Test Thoroughly** - Run all notebooks in Jupyter
3. **Add Exercises** - Create practice problems with solutions
4. **Plan Intermediate** - Start designing 02-intermediate course

---

## 💡 Tips

- **Use `Shift+Enter`** to run Jupyter cells
- **Restart kernel** if code behaves unexpectedly: Kernel → Restart
- **Clear outputs** before committing: Cell → All Output → Clear
- **Save regularly** when working in notebooks
- **Keep generator scripts updated** when making changes

---

## 🆘 Troubleshooting

### Jupyter Not Found
```bash
pip install jupyter
```

### Wrong Directory
```bash
cd C:\Users\Admin\projects\python-master-course
```

### Notebooks Not Loading
- Check file permissions
- Verify .ipynb file is valid JSON
- Try regenerating with script

### Can't Run Code Cells
- Check Python kernel is running
- Restart kernel and try again
- Verify Python installation

---

**Quick Links:**
- 📖 [Full README](README.md)
- ✅ [Setup Complete](SETUP_COMPLETE.md)
- 📚 [Beginner Index](01-beginner/INDEX.md)
