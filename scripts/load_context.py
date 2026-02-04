#!/usr/bin/env python3
"""
Load project context files into a structured format for the agent.
"""

import os
import json
import sys
from pathlib import Path


def load_context(project_root=None):
    """Load all context files from the project."""
    if project_root is None:
        # Try to find project root
        from detect_project import find_project_root
        detection = find_project_root()
        if not detection["is_project"]:
            return {"error": "No project found in current directory"}
        project_root = detection["project_root"]
    
    context_path = Path(project_root) / ".context"
    
    context = {
        "project_root": project_root,
        "loaded_files": [],
        "identity": {},
        "memory": "",
        "tools": "",
        "heartbeat": "",
        "additional_memories": []
    }
    
    # Load IDENTITY.md
    identity_file = context_path / "IDENTITY.md"
    if identity_file.exists():
        content = identity_file.read_text()
        context["identity"] = parse_identity(content)
        context["loaded_files"].append("IDENTITY.md")
    
    # Load MEMORY.md
    memory_file = context_path / "MEMORY.md"
    if memory_file.exists():
        context["memory"] = memory_file.read_text()
        context["loaded_files"].append("MEMORY.md")
    
    # Load TOOLS.md
    tools_file = context_path / "TOOLS.md"
    if tools_file.exists():
        context["tools"] = tools_file.read_text()
        context["loaded_files"].append("TOOLS.md")
    
    # Load HEARTBEAT.md
    heartbeat_file = context_path / "HEARTBEAT.md"
    if heartbeat_file.exists():
        context["heartbeat"] = heartbeat_file.read_text()
        context["loaded_files"].append("HEARTBEAT.md")
    
    # Load additional memories from memory/
    memory_dir = context_path / "memory"
    if memory_dir.exists() and memory_dir.is_dir():
        for mem_file in sorted(memory_dir.glob("*.md")):
            context["additional_memories"].append({
                "file": mem_file.name,
                "content": mem_file.read_text()
            })
            context["loaded_files"].append(f"memory/{mem_file.name}")
    
    return context


def parse_identity(content):
    """Parse IDENTITY.md content into structured data."""
    identity = {}
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('- **Name:**'):
            identity['name'] = line.split(':**')[1].strip()
        elif line.startswith('- **Emoji:**'):
            identity['emoji'] = line.split(':**')[1].strip()
        elif line.startswith('- **Description:**'):
            identity['description'] = line.split(':**')[1].strip()
        elif line.startswith('- **Created:**'):
            identity['created'] = line.split(':**')[1].strip()
    return identity


if __name__ == "__main__":
    context = load_context()
    print(json.dumps(context, indent=2))
