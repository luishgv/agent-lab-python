import functools
import random

from app.data import (
    FREE_SPACE,
    MAX_QUESTION_LENGTH,
    MIN_QUESTION_LENGTH,
    QUESTIONS,
    REQUIRED_QUESTION_COUNT,
)
from app.models import BingoLine, BingoSquareData

BOARD_SIZE = 5
CENTER_INDEX = 12  # 5x5 grid, center is index 12 (row 2, col 2)


def parse_custom_questions(raw_text: str) -> list[str]:
    """Parse newline-separated question text into a cleaned, de-duplicated list.

    Blank lines are dropped, surrounding whitespace is stripped, and
    duplicate questions (case-insensitive) are removed while preserving the
    order in which they first appeared.
    """
    seen: set[str] = set()
    questions: list[str] = []
    for line in raw_text.splitlines():
        text = line.strip()
        if not text:
            continue
        key = text.casefold()
        if key in seen:
            continue
        seen.add(key)
        questions.append(text)
    return questions


def validate_questions(questions: list[str]) -> list[str]:
    """Validate custom questions and return a list of error messages.

    An empty list of errors means the questions are valid and can be used
    to generate a board.
    """
    errors: list[str] = []

    if len(questions) < REQUIRED_QUESTION_COUNT:
        errors.append(
            f"Enter at least {REQUIRED_QUESTION_COUNT} unique questions "
            f"(got {len(questions)})."
        )

    if any(len(q) < MIN_QUESTION_LENGTH for q in questions):
        errors.append(
            f"Each question must be at least {MIN_QUESTION_LENGTH} characters long."
        )

    if any(len(q) > MAX_QUESTION_LENGTH for q in questions):
        errors.append(
            f"Each question must be at most {MAX_QUESTION_LENGTH} characters long."
        )

    return errors


def generate_board(questions: list[str] | None = None) -> list[BingoSquareData]:
    """Generate a new 5x5 bingo board.

    Uses the provided question pool when given (must contain at least
    ``REQUIRED_QUESTION_COUNT`` questions), otherwise falls back to the
    default question bank.
    """
    pool = questions if questions else QUESTIONS
    sampled = iter(random.sample(pool, REQUIRED_QUESTION_COUNT))
    return [
        BingoSquareData(id=i, text=FREE_SPACE, is_marked=True, is_free_space=True)
        if i == CENTER_INDEX
        else BingoSquareData(id=i, text=next(sampled))
        for i in range(BOARD_SIZE * BOARD_SIZE)
    ]


def toggle_square(
    board: list[BingoSquareData], square_id: int
) -> list[BingoSquareData]:
    """Toggle a square's marked state. Returns a new board list."""
    return [
        sq.model_copy(update={"is_marked": not sq.is_marked})
        if sq.id == square_id and not sq.is_free_space
        else sq
        for sq in board
    ]


@functools.cache
def _get_winning_lines() -> tuple[BingoLine, ...]:
    """Get all possible winning lines (cached)."""
    lines: list[BingoLine] = []

    for row in range(BOARD_SIZE):
        squares = [row * BOARD_SIZE + col for col in range(BOARD_SIZE)]
        lines.append(BingoLine(type="row", index=row, squares=squares))

    for col in range(BOARD_SIZE):
        squares = [row * BOARD_SIZE + col for row in range(BOARD_SIZE)]
        lines.append(BingoLine(type="column", index=col, squares=squares))

    lines.append(BingoLine(type="diagonal", index=0, squares=[0, 6, 12, 18, 24]))
    lines.append(BingoLine(type="diagonal", index=1, squares=[4, 8, 12, 16, 20]))

    return tuple(lines)


def check_bingo(board: list[BingoSquareData]) -> BingoLine | None:
    """Check if there's a bingo and return the winning line."""
    if len(board) < BOARD_SIZE * BOARD_SIZE:
        return None
    return next(
        (
            line
            for line in _get_winning_lines()
            if all(board[idx].is_marked for idx in line.squares)
        ),
        None,
    )


def get_winning_square_ids(line: BingoLine | None) -> set[int]:
    """Get the square IDs that are part of a winning line."""
    return set(line.squares) if line else set()
