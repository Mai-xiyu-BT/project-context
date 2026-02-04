#!/usr/bin/env python3
"""
Detect if current directory is part of a project with .context/ folder.
Searches current and parent directories for .context/.
"""

import os
import json
import sys
from pathlib import Path


def find_project_root(start_path=None):
    """Find the project root by looking for .context/ folder."""
    if start_path is None:
        start_path = os.getcwd()
    
    current = Path(start_path).resolve()
    
    # Search up to 10 parent directories
    for _ in range(10):
        context_path = current / ".context"
        if context_path.exists() and context_path.is_dir():
            return {
                "is_project": True,
                "context_path": str(context_path),
                "project_root": str(current),
                "project_name": current.name
            }
        
        # Move to parent
        parent = current.parent
        if parent == current:  # Reached root
            break
        current = parent
    
    return {
        "is_project": False,
        "context_path": None,
        "project_root": None,
        "project_name": None
    }


if __name__ == "__main__":
    result = find_project_root()
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["is_project"] else 1)
