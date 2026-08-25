# Copilot Workspace Instructions

## Development Checklist

Before committing any changes, ensure:

- [ ] `uv run ruff check .` passes with no errors
- [ ] `uv run pytest` passes
- [ ] Code follows Python conventions (snake_case, type hints)
- [ ] No unused variables or imports

## Project Overview

**Soc Ops** is a Social Bingo game built with Python (FastAPI + Jinja2 + HTMX). Players find people who match questions to mark squares and get 5 in a row.

## Architecture

```
app/
├── templates/       # Jinja2 HTML templates
│   ├── base.html
│   ├── home.html
│   └── components/  # bingo_board, bingo_modal, game_screen, start_screen
├── static/          # CSS & JS assets
├── models.py        # Pydantic models (GameState, BingoSquare)
├── game_logic.py    # Board generation & bingo detection
├── game_service.py  # Session management (GameSession)
├── data.py          # Question bank
└── main.py          # FastAPI routes & HTMX endpoints
tests/
├── test_api.py      # API endpoint tests (httpx + TestClient)
└── test_game_logic.py  # Game logic unit tests
```

## Key Commands

```bash
uv run uvicorn app.main:app --reload --port 8000  # Run dev server
uv run pytest                                       # Run tests
uv run ruff check .                                 # Lint
```

## Styling

Uses custom CSS utility classes (Tailwind-like) in `app/static/css/app.css`:
- Layout: `.flex`, `.grid`, `.items-center`
- Spacing: `.p-4`, `.mb-2`, `.mx-auto`
- Colors: `.bg-accent`, `.bg-marked`, `.text-gray-700`

## State Management

- `GameSession` manages game state server-side
- State persisted via signed cookies (itsdangerous)
- HTMX handles partial page updates without full reloads

## Design Guide

When changing the frontend:

- Preserve the existing Jinja2 component structure, HTMX interactions, and utility-class approach.
- Design for the actual social bingo workflow: make the board, current state, and next action immediately scannable.
- Use distinctive typography and a deliberate color palette with CSS variables; avoid default system fonts, purple-on-white gradients, and interchangeable dashboard layouts.
- Build atmosphere with restrained patterns, gradients, or contextual shapes instead of relying on a flat background. Keep cards limited to repeated items, modals, and genuinely framed tools.
- Add a small number of meaningful CSS animations for page-load or state changes, while respecting `prefers-reduced-motion`.
- Keep controls keyboard accessible with visible focus states, clear labels, adequate contrast, and touch-friendly target sizes.
- Use stable responsive dimensions for the 5x5 board so labels, icons, and marked states never shift the layout on mobile or desktop.
- Verify that text remains inside its containers and that adjacent controls do not overlap at narrow widths.
