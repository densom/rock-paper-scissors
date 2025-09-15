# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Rock Paper Scissors learning project - a progressive Python game to teach programming concepts to a 12-year-old. Starts with basic CLI gameplay and evolves into web applications with AI opponents.

## Development Setup

### Python Environment
```bash
# Create virtual environment
uv venv

# Activate virtual environment (Windows)
.venv\Scripts\activate

# Add dependencies to the project
uv add <package-name>
# Add development dependencies
uv add --dev <package-name>
# Install all dependencies from pyproject.toml
uv sync

# Run the game
uv run python src/main.py

# Run tests (when added)
uv run python -m pytest tests/

# Code formatting (when added)
uv run black src/
uv run flake8 src/
```

## Project Structure

```
├── src/                    # Main game code
│   ├── main.py            # Entry point
│   ├── game/              # Game logic modules
│   └── ai/                # AI opponent implementations
├── tests/                 # Unit tests
├── docs/                  # Project documentation
│   └── BACKLOG.md         # Feature backlog for Linear.app
├── web/                   # Web interface (future phases)
├── pyproject.toml         # Project configuration and dependencies (uv preferred)
└── requirements.txt       # Python dependencies (legacy support)
```

## Architecture

- **Phase 1**: Simple procedural Python with basic game logic
- **Phase 2**: Object-oriented design with AI classes
- **Phase 3**: Web framework integration (Flask/FastAPI)
- **Phase 4**: Real-time features with WebSockets

## Development Guidelines

- Keep code simple and well-commented for learning purposes
- Each phase should build incrementally on the previous
- Focus on teaching one concept at a time
- Include plenty of print statements for debugging and learning

## Git Commit Guidelines

- When creating commits, use descriptive messages that explain the changes
- Do NOT include the 🤖 Generated with [Claude Code](https://claude.ai/code) footer
- Do NOT include Co-Authored-By: Claude attribution
- Keep commit messages concise but informative

## Linear.app Project Management

This project uses Linear.app for tracking development progress and managing the educational backlog.

### Linear Configuration
- **Project**: Rock-Paper-Scissors (configured for educational learning progression)
- **Team**: Densom1
- **Current Phase**: Phase 1 - Foundation Features

### Educational Labels System
- **Phase Labels**: Phase-1 (Green), Phase-2 (Blue), Phase-3 (Orange), Phase-4 (Purple), Phase-5 (Pink)
- **Complexity Labels**: beginner (Light Green), intermediate (Yellow), advanced (Red)
- **Priority Labels**: p0 (Must have), p1 (Should have), p2 (Could have), p3 (Won't have)
- **Feature Labels**: foundation, cli, ai, oop, web, multiplayer, etc.

### Issue Management
- All 14 user stories from docs/BACKLOG.md have been created as Linear issues (DEN-9 through DEN-22)
- **RPS-001: Basic CLI Game** (DEN-9) is the starting point, set to "Todo" status
- Issues follow learning progression with proper dependencies
- Story points included for educational time estimation

### Linear Usage Guidelines
- Use the linear-project-manager agent for all Linear.app configuration and issue management
- The linear-project-manager agent should ONLY handle Linear tasks, not development environment setup or code implementation
- Update issue status as development progresses through each learning phase
- Reference Linear issue numbers (e.g., DEN-9) in commit messages when implementing features

## Other Guidance from the # Memory Commands
