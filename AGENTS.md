# Soc Ops Agent Guide

## Mandatory Development Checklist

Before finishing any change, run all three checks:

- [ ] Lint: `uv run ruff check .`
- [ ] Build: `uv run python -m compileall app`
- [ ] Test: `uv run pytest`

Use Python 3.13+ and `uv`. Run the narrowest relevant test first. Do not commit unless asked.

Soc Ops is a FastAPI/Jinja2/HTMX Social Bingo app. `app/main.py` owns routes and templates; `app/game_service.py` owns session state; `app/game_logic.py` contains pure board rules; `app/models.py` contains Pydantic models; `app/data.py` contains questions.

Keep game rules independent from HTTP and templates. Test pure logic in `tests/test_game_logic.py` and routes/rendered responses in `tests/test_api.py`.

The board has 25 squares; index 12 is the marked free space. Winning lines are five rows, five columns, and two diagonals. Sessions are intentionally in memory; the signed cookie stores only the session ID.

For frontend work, follow the existing Jinja2 component, HTMX, and utility-class patterns in `app/static/css/app.css`. Also follow [frontend instructions](.github/instructions/frontend-design.instructions.md) and [CSS instructions](.github/instructions/css-utilities.instructions.md). Never use the Simple Browser; run `uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000` instead.

See [README.md](README.md), [workshop/GUIDE.md](workshop/GUIDE.md), and [CONTRIBUTING.md](CONTRIBUTING.md) for project context and contribution rules.
