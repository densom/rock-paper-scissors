# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Rock Paper Scissors learning project - a progressive Python game to teach programming concepts to a 12-year-old. Starts with basic CLI gameplay and evolves into web applications with AI opponents.

## Development Setup

### Python Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies (as they're added)
pip install -r requirements.txt

# Run the game
python src/main.py

# Run tests (when added)
python -m pytest tests/

# Code formatting (when added)
black src/
flake8 src/
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
└── requirements.txt       # Python dependencies
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
- Include the 🤖 Generated with [Claude Code](https://claude.ai/code) footer
- Do NOT include Co-Authored-By: Claude attribution
- Keep commit messages concise but informative