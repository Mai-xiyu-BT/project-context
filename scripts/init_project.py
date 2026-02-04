#!/usr/bin/env python3
"""
Initialize a new project context structure in the current directory.
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path


def init_project(name=None, force=False):
    """Create a new .context/ structure in current directory."""
    current_dir = Path.cwd()
    context_path = current_dir / ".context"
    
    # Check if already exists
    if context_path.exists() and not force:
        print(f"Error: .context/ already exists in {current_dir}")
        print("Use --force to overwrite")
        sys.exit(1)
    
    # Create directories
    context_path.mkdir(exist_ok=True)
    (context_path / "memory").mkdir(exist_ok=True)
    
    # Use directory name if no name provided
    if not name:
        name = current_dir.name
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Create IDENTITY.md
    identity_content = f"""# Project Identity

- **Name:** {name}
- **Emoji:** 📁
- **Description:** 
- **Created:** {date_str}
"""
    (context_path / "IDENTITY.md").write_text(identity_content)
    
    # Create MEMORY.md
    memory_content = f"""# Project Memory

## Key Decisions

*Add important decisions here*

## Known Issues

*Document known problems and workarounds*

## TODO

- [ ] 
"""
    (context_path / "MEMORY.md").write_text(memory_content)
    
    # Create TOOLS.md
    tools_content = """# Project Tools

## Commands

*Add frequently used commands*

## Configuration

*Document project-specific configurations*

## Notes

*Any other project-specific notes*
"""
    (context_path / "TOOLS.md").write_text(tools_content)
    
    # Create HEARTBEAT.md (optional, can be empty)
    heartbeat_content = """# Project Heartbeat

*Add periodic tasks specific to this project*
*Leave empty if not needed*
"""
    (context_path / "HEARTBEAT.md").write_text(heartbeat_content)
    
    print(f"✓ Initialized project context in {context_path}")
    print(f"  Project name: {name}")
    print(f"\nNext steps:")
    print(f"  1. Edit .context/IDENTITY.md to set project details")
    print(f"  2. Add initial notes to .context/MEMORY.md")
    print(f"  3. Configure tools in .context/TOOLS.md")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize project context")
    parser.add_argument("--name", "-n", help="Project name (defaults to directory name)")
    parser.add_argument("--force", "-f", action="store_true", help="Overwrite existing context")
    
    args = parser.parse_args()
    init_project(args.name, args.force)
