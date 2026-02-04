---
name: project-context
description: Automatic project context detection and management for OpenClaw sessions. Use when working in a project directory that has a .context/ folder or when the user mentions project-specific memories, configurations, or workflows. Automatically loads project identity, memory files, and tool configurations to maintain continuity across sessions. Ideal for multi-project workflows where each project has unique requirements, coding standards, or accumulated knowledge.
---

# Project Context

## Overview

Automatically detects and loads project-specific context when working in directories containing a `.context/` folder. Maintains project identity, memories, and configurations across sessions.

## When This Skill Activates

- Current working directory contains a `.context/` subdirectory
- User mentions "project context", "project memory", or "project config"
- Working on a known project that has been configured previously

## Core Capabilities

### 1. Project Detection

Automatically identifies if current directory is part of a project:

```bash
# Check if .context/ exists in current or parent directories
python3 scripts/detect_project.py
```

Returns: `{ "is_project": true/false, "context_path": "...", "project_root": "..." }`

### 2. Context Loading

Loads all project-specific files into the session:

```bash
# Load project context
python3 scripts/load_context.py
```

Loads in priority order:
1. `.context/IDENTITY.md` - Project identity (name, description, emoji)
2. `.context/MEMORY.md` - Long-term project memory
3. `.context/TOOLS.md` - Project-specific tool configurations
4. `.context/memory/*.md` - Additional memory files
5. `.context/HEARTBEAT.md` - Project-specific periodic tasks

### 3. Context Saving

Saves current session insights back to project memory:

```bash
# Save a memory to the project
python3 scripts/save_memory.py "Fixed the authentication bug in user.py"

# Save with category
python3 scripts/save_memory.py "API rate limit: 100 req/min" --category api
```

### 4. Project Initialization

Creates a new project context structure:

```bash
# Initialize project context in current directory
python3 scripts/init_project.py

# With custom name
python3 scripts/init_project.py --name "My Awesome Project"
```

Creates:
```
.context/
├── IDENTITY.md      # Project identity
├── MEMORY.md        # Long-term memory
├── TOOLS.md         # Tool configurations
├── HEARTBEAT.md     # Periodic tasks (optional)
└── memory/          # Additional memories
```

## Workflow

### Starting Work on a Project

1. Navigate to project directory
2. Skill auto-detects `.context/` folder
3. Loads all context files into session
4. Acknowledge loaded context to user

### During Session

1. Work normally
2. Important discoveries are auto-saved to project memory
3. User can manually save: `Remember this for the project: ...`

### Ending Session

1. Summarize key changes/decisions
2. Offer to save summary to project memory
3. Optional: Update HEARTBEAT.md with new periodic tasks

## File Formats

### IDENTITY.md
```markdown
# Project Identity

- **Name:** MyProject
- **Emoji:** 🚀
- **Description:** A web scraping tool
- **Created:** 2024-01-15
```

### MEMORY.md
```markdown
# Project Memory

## Key Decisions
- Using Scrapy instead of BeautifulSoup for better performance

## Known Issues
- Rate limiting on target site (handled with delays)

## TODO
- [ ] Add proxy rotation
- [ ] Implement retry logic
```

### TOOLS.md
```markdown
# Project Tools

## Commands
- `make scrape` - Run the scraper
- `make test` - Run tests

## API Keys
- Stored in .env (not in context!)

## Database
- SQLite at ./data/scraped.db
```

## Scripts Reference

| Script | Purpose |
|--------|---------|
| `detect_project.py` | Find project root and .context/ folder |
| `load_context.py` | Load all context files into session |
| `save_memory.py` | Save a memory entry to project |
| `init_project.py` | Create new project context structure |
| `list_projects.py` | List all known projects |

## Best Practices

1. **One project per directory** - Don't nest .context/ folders
2. **Keep MEMORY.md concise** - Move old memories to `memory/YYYY-MM-DD.md`
3. **No secrets in context** - Use .env files, never commit API keys
4. **Regular cleanup** - Archive old memories monthly
