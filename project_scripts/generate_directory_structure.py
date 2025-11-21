#!/usr/bin/env python3
"""
Generate and display the directory structure of the python-master-course project.
Run this script whenever the directory structure changes to keep documentation up-to-date.
"""

import os
from pathlib import Path


def generate_tree(directory: Path, prefix: str = "", is_last: bool = True) -> list[str]:
    """
    Generate a tree structure of directories.
    
    Args:
        directory: Path object pointing to the directory
        prefix: Prefix for tree lines
        is_last: Whether this is the last item in current level
        
    Returns:
        List of lines representing the tree structure
    """
    lines = []
    
    # Skip hidden directories and common exclusions
    excluded_dirs = {'.git', '.venv', 'venv', '__pycache__', '.pytest_cache', 
                     'node_modules', '.idea', '.vscode', 'dist', 'build'}
    
    dir_name = directory.name if directory.name else directory
    connector = "└── " if is_last else "├── "
    lines.append(f"{prefix}{connector}{dir_name}/")
    
    try:
        # Get all subdirectories, sorted alphabetically
        subdirs = sorted([
            d for d in directory.iterdir() 
            if d.is_dir() and d.name not in excluded_dirs
        ])
        
        # Process each subdirectory
        for idx, subdir in enumerate(subdirs):
            is_last_subdir = (idx == len(subdirs) - 1)
            extension = "    " if is_last else "│   "
            lines.extend(
                generate_tree(subdir, prefix + extension, is_last_subdir)
            )
            
    except PermissionError:
        pass
    
    return lines


def count_files_in_dir(directory: Path) -> int:
    """Count files (not directories) in a directory."""
    try:
        return len([f for f in directory.iterdir() if f.is_file()])
    except PermissionError:
        return 0


def main():
    """Main function to generate and print directory structure."""
    # Get the project root (parent of project_scripts)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Define main directories in order
    main_dirs = [
        "01-beginner",
        "02-intermediate",
        "03-advanced",
        "04-libraries",
        "05-applications",
        "06-projects",
        "examples",
        "project_scripts",
        "resources"
    ]
    
    print("python-master-course/")
    
    for idx, dir_name in enumerate(main_dirs):
        dir_path = project_root / dir_name
        is_last = (idx == len(main_dirs) - 1)
        connector = "└──" if is_last else "├── "
        
        if dir_path.exists():
            file_count = count_files_in_dir(dir_path)
            count_str = f" ({file_count} files)" if file_count > 0 else ""
            print(f"{connector}{dir_name}/{count_str}")
        else:
            print(f"{connector}{dir_name}/")
    
    print()
    
    # Count total files and directories
    total_files = len(list(project_root.rglob('*.ipynb'))) + len(list(project_root.rglob('*.py'))) + len(list(project_root.rglob('*.md')))
    total_dirs = len([d for d in project_root.rglob('*') if d.is_dir()])
    
    print(f"Total: {total_dirs} directories, {total_files} files (.ipynb, .py, .md)")
    print()
    print("Generated:", __file__)


if __name__ == "__main__":
    main()
