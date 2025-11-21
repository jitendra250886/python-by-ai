#!/usr/bin/env python3
"""
Quick start script for Python Master Course.
Opens Jupyter notebook in the specified course directory.
"""

import sys
import subprocess
from pathlib import Path


def main():
    """Launch Jupyter notebook for the course."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Available course levels
    courses = {
        "1": ("01-beginner", "Beginner - Python Fundamentals (20 lessons)"),
        "2": ("02-intermediate", "Intermediate - Advanced Concepts (Coming Soon)"),
        "3": ("03-advanced", "Advanced - Expert Techniques (Coming Soon)"),
        "4": ("04-libraries", "Libraries & Frameworks (Coming Soon)"),
        "5": ("05-applications", "Real-World Applications (Coming Soon)"),
        "6": ("06-projects", "Hands-On Projects (Coming Soon)"),
    }
    
    print("=" * 60)
    print("Python Master Course - Quick Start")
    print("=" * 60)
    print()
    
    # Check if a course level was provided as argument
    if len(sys.argv) > 1:
        choice = sys.argv[1]
    else:
        # Display menu
        print("Select a course level:")
        print()
        for key, (folder, description) in courses.items():
            status = "✅" if folder == "01-beginner" else "🚧"
            print(f"  {key}. {status} {description}")
        print()
        print("  0. Exit")
        print()
        
        choice = input("Enter your choice (1-6): ").strip()
    
    if choice == "0":
        print("Goodbye!")
        return
    
    if choice not in courses:
        print(f"❌ Invalid choice: {choice}")
        return
    
    folder, description = courses[choice]
    course_dir = project_root / folder
    
    if not course_dir.exists():
        print(f"❌ Course directory not found: {course_dir}")
        return
    
    print(f"\n🚀 Launching {description}...")
    print(f"📂 Directory: {course_dir}")
    print()
    print("Opening Jupyter Notebook...")
    print("Press Ctrl+C in the terminal to stop the server when done.")
    print()
    
    try:
        # Launch Jupyter notebook
        subprocess.run(["jupyter", "notebook", str(course_dir)], check=True)
    except FileNotFoundError:
        print("❌ Jupyter is not installed or not in PATH.")
        print("Install it with: pip install jupyter")
    except KeyboardInterrupt:
        print("\n\n✅ Jupyter server stopped.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error launching Jupyter: {e}")


if __name__ == "__main__":
    main()
