# 🧠 Project Context

[![ClawHub](https://img.shields.io/badge/ClawHub-Available-blue)](https://clawhub.com)
[![License](https://img.shields.io/badge/License-PolyForm%20Noncommercial%201.0.0-lightgrey)](LICENSE)

An [OpenClaw](https://openclaw.ai) skill for automatic project context detection and management. Maintain project identity, memories, and configurations across AI sessions.

## Features

- 🔍 **Automatic Detection** - Detects `.context/` folders in current or parent directories
- 📝 **Context Loading** - Auto-loads project identity, memories, and tool configurations
- 💾 **Smart Saving** - Save important discoveries back to project memory
- 🚀 **Easy Init** - One command to set up project context
- 🗂️ **Multi-Project** - Seamlessly work across multiple projects

## Installation

```bash
clawhub install project-context
```

## Quick Start

### 1. Initialize Project Context

```bash
# In your project directory
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/Mai-xiyu-BT/project-context/main/scripts/init_project.py)"
```

Or manually:
```bash
cd /your/project/path
python3 scripts/init_project.py --name "My Project"
```

### 2. Edit Your Context

```bash
.context/
├── IDENTITY.md      # Project name, emoji, description
├── MEMORY.md        # Long-term memory & decisions
├── TOOLS.md         # Commands & configurations
├── HEARTBEAT.md     # Periodic tasks (optional)
└── memory/          # Archived memories
```

### 3. Start Working

When you enter the project directory, OpenClaw automatically:
1. Detects the `.context/` folder
2. Loads all context files
3. Knows your project's history and preferences

## File Reference

### IDENTITY.md
```markdown
- **Name:** MyProject
- **Emoji:** 🚀
- **Description:** A web scraping tool
- **Created:** 2024-01-15
```

### MEMORY.md
```markdown
## Key Decisions
- Using PostgreSQL instead of MongoDB

## Known Issues
- Rate limiting on API calls

## TODO
- [ ] Implement caching
```

### TOOLS.md
```markdown
## Commands
- `make dev` - Start development server
- `make test` - Run test suite

## Database
- PostgreSQL at localhost:5432/mydb
```

## CLI Scripts

| Script | Purpose |
|--------|---------|
| `detect_project.py` | Find project root and `.context/` folder |
| `load_context.py` | Load all context files |
| `save_memory.py` | Save a memory entry |
| `init_project.py` | Create new project context |
| `list_projects.py` | List all known projects |

## Why Project Context?

AI assistants have short-term memory. When you start a new session, they forget:
- Your project's coding standards
- Decisions made in previous sessions
- Tool configurations and aliases
- Ongoing TODOs and issues

**Project Context solves this** by maintaining persistent, project-specific knowledge that auto-loads when you work.

## License

This project is licensed under the **PolyForm Noncommercial License 1.0.0**.

- ✅ Personal use
- ✅ Educational use
- ✅ Open source projects
- ❌ Commercial use (without authorization)

For commercial licensing, please [open an issue](../../issues).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

- 🐛 [Report bugs](../../issues)
- 💡 [Request features](../../issues)
- 💬 [Discussions](../../discussions)

---

Made with ❤️ for the OpenClaw community
