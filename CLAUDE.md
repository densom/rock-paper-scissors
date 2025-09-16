# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 🎮 Project Overview

**Rock Paper Scissors Learning Project** - A progressive Python game designed to teach programming concepts to a 12-year-old. The project evolves through phases, starting with basic CLI gameplay and advancing to web applications with AI opponents.

### Learning Phases
- **Phase 1**: Simple procedural Python with basic game logic
- **Phase 2**: Object-oriented design with AI classes
- **Phase 3**: Web framework integration (Flask/FastAPI)
- **Phase 4**: Real-time features with WebSockets

## 🚀 Quick Start

### Setup & Run
```bash
# Setup environment
uv venv && .venv\Scripts\activate && uv sync

# Run the game
uv run python src/main.py

# Run tests
uv run python -m pytest tests/

# Code formatting
uv run black src/ && uv run flake8 src/
```

### Project Structure
```
├── src/                    # Main game code
│   ├── main.py            # Entry point
│   ├── game/              # Game logic modules
│   └── ai/                # AI opponent implementations
├── tests/                 # Unit tests
├── docs/BACKLOG.md         # Feature backlog for Linear.app
├── web/                   # Web interface (future phases)
└── pyproject.toml         # Project configuration
```

## 💻 Development Workflow

### Development Guidelines
- Keep code simple and well-commented for learning purposes
- Build incrementally on previous phases
- Focus on teaching one concept at a time
- Include print statements for debugging and learning

### Python Environment Management
| Command | Purpose |
|---------|---------|
| `uv add <package>` | Add runtime dependency |
| `uv add --dev <package>` | Add development dependency |
| `uv sync` | Install all dependencies from pyproject.toml |

## 🔄 Git & Linear Integration

### Branch Naming
Format: `<issue-id>-title`
- Example: `den-9-rps-001-basic-cli-game`

### Commit Messages
**Format**: `<magic-word> <issue-id>: <descriptive message>`

**Examples:**
- `fixes DEN-9: implement basic CLI game loop`
- `part of DEN-10: add player input validation`
- `closes DEN-11: implement game scoring system`

### Commit Rules
- ✅ Reference Linear issue ID in every commit
- ✅ Use descriptive messages explaining changes
- ❌ No Claude Code footer or attribution
- ❌ Keep messages concise but informative

## 📋 Linear.app Project Management

### Project Configuration
- **Project**: Rock-Paper-Scissors
- **Team**: Densom1
- **Current Phase**: Phase 1 - Foundation Features

### Issue Workflow
1. **Start Work**: Move issue to "In Progress"
2. **Complete Code**: Move to "In Review"
3. **Final Closure**: External process moves to "Done"

### Agent Usage
- Use `linear-project-manager` agent for all Linear.app tasks
- Agent handles ONLY Linear management, not code implementation
- Always assign issues to the Rock-Paper-Scissors project

---

## 📚 Reference

### Linear Magic Words
**Closing** (closes issue when merged): `closes`, `fixes`, `resolves`, `completes`
**Contributing** (links without closing): `part of`, `contributes to`, `references`

### Educational Label System
| Type | Labels |
|------|--------|
| **Phase** | Phase-1 (Green), Phase-2 (Blue), Phase-3 (Orange), Phase-4 (Purple) |
| **Complexity** | beginner (Light Green), intermediate (Yellow), advanced (Red) |
| **Priority** | p0 (Must), p1 (Should), p2 (Could), p3 (Won't) |
| **Feature** | foundation, cli, ai, oop, web, multiplayer |

### Workflow Automation
- Branch push → Issue moves to "In Progress"
- Merge to master → Issue moves to "Done"

## Other Guidance from the # Memory Commands
