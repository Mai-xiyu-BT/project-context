#!/usr/bin/env python3
"""
List all known projects by searching for .context/ directories.
"""

import os
import json
from pathlib import Path


def find_projects(search_paths=None, max_depth=3):
    """Find all projects with .context/ folders."""
    if search_paths is None:
        # Default: search common project locations
        home = Path.home()
        search_paths = [
            home / "projects",
            home / "workspace",
            home / "code",
            home / "dev",
            home / "repos",
            home / ".openclaw" / "workspace",
        ]
    
    projects = []
    
    for base_path in search_paths:
        if not base_path.exists():
            continue
        
        # Search for .context directories
        try:
            for item in base_path.rglob(".context"):
                if item.is_dir():
                    project_root = item.parent
                    identity_file = item / "IDENTITY.md"
                    
                    project_info = {
                        "path": str(project_root),
                        "name": project_root.name,
                        "identity": {}
                    }
                    
                    # Try to read identity
                    if identity_file.exists():
                        content = identity_file.read_text()
                        for line in content.split('\n'):
                            if line.startswith('- **Name:**'):
                                project_info["name"] = line.split(':**')[1].strip()
                            elif line.startswith('- **Emoji:**'):
                                project_info["identity"]["emoji"] = line.split(':**')[1].strip()
                            elif line.startswith('- **Description:**'):
                                project_info["identity"]["description"] = line.split(':**')[1].strip()
                    
                    projects.append(project_info)
        except PermissionError:
            continue
    
    return projects


if __name__ == "__main__":
    projects = find_projects()
    
    if not projects:
        print("No projects found.")
        print("\nTo create a project:")
        print("  1. cd /path/to/your/project")
        print("  2. python3 scripts/init_project.py")
    else:
        print(f"Found {len(projects)} project(s):\n")
        for p in projects:
            emoji = p["identity"].get("emoji", "📁")
            name = p["name"]
            path = p["path"]
            desc = p["identity"].get("description", "")
            print(f"{emoji} {name}")
            print(f"   Path: {path}")
            if desc:
                print(f"   {desc}")
            print()
