#!/usr/bin/env python3
"""
Save a memory entry to the project's MEMORY.md or a dated memory file.
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path


def save_memory(content, category=None, dated=False):
    """Save a memory to the project context."""
    # Find project root
    from detect_project import find_project_root
    detection = find_project_root()
    
    if not detection["is_project"]:
        print("Error: No project found in current directory", file=sys.stderr)
        sys.exit(1)
    
    project_root = detection["project_root"]
    context_path = Path(project_root) / ".context"
    
    # Ensure memory directory exists
    memory_dir = context_path / "memory"
    memory_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Format the entry
    if category:
        entry = f"\n## [{timestamp}] {category.upper()}\n\n{content}\n"
    else:
        entry = f"\n## [{timestamp}]\n\n{content}\n"
    
    # Determine target file
    if dated:
        target_file = memory_dir / f"{date_str}.md"
        if not target_file.exists():
            target_file.write_text(f"# Memory Log - {date_str}\n")
    else:
        target_file = context_path / "MEMORY.md"
        if not target_file.exists():
            target_file.write_text("# Project Memory\n")
    
    # Append to file
    with open(target_file, 'a') as f:
        f.write(entry)
    
    print(f"✓ Saved to {target_file.relative_to(Path.cwd())}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Save a memory to the project context")
    parser.add_argument("content", help="The memory content to save")
    parser.add_argument("--category", "-c", help="Category for the memory")
    parser.add_argument("--dated", "-d", action="store_true", help="Save to dated file instead of MEMORY.md")
    
    args = parser.parse_args()
    save_memory(args.content, args.category, args.dated)
