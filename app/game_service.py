from dataclasses import dataclass, field

from app.game_logic import (
    check_bingo,
    generate_board,
    get_winning_square_ids,
    parse_custom_questions,
    toggle_square,
    validate_questions,
)
from app.models import BingoLine, BingoSquareData, GameState


@dataclass
class GameSession:
    """Holds the state for a single game session."""

    game_state: GameState = GameState.START
    board: list[BingoSquareData] = field(default_factory=list)
    winning_line: BingoLine | None = None
    show_bingo_modal: bool = False
    quiz_errors: list[str] = field(default_factory=list)
    pending_custom_input: str = ""
    used_custom_questions: bool = False

    @property
    def winning_square_ids(self) -> set[int]:
        return get_winning_square_ids(self.winning_line)

    @property
    def has_bingo(self) -> bool:
        return self.game_state == GameState.BINGO

    def enter_customize(self) -> None:
        """Show the custom quiz question entry screen."""
        self.game_state = GameState.CUSTOMIZE
        self.quiz_errors = []

    def start_game(self, raw_custom_questions: str | None = None) -> None:
        """Start a new game.

        If ``raw_custom_questions`` is blank or omitted, the default question
        bank is used (safe fallback). If it is provided but fails validation,
        the game stays on the customize screen with clear error messages
        instead of starting.
        """
        questions: list[str] | None = None

        if raw_custom_questions and raw_custom_questions.strip():
            parsed = parse_custom_questions(raw_custom_questions)
            errors = validate_questions(parsed)
            if errors:
                self.game_state = GameState.CUSTOMIZE
                self.quiz_errors = errors
                self.pending_custom_input = raw_custom_questions
                return
            questions = parsed

        self.board = generate_board(questions)
        self.winning_line = None
        self.game_state = GameState.PLAYING
        self.show_bingo_modal = False
        self.quiz_errors = []
        self.pending_custom_input = ""
        self.used_custom_questions = questions is not None

    def handle_square_click(self, square_id: int) -> None:
        if self.game_state != GameState.PLAYING:
            return
        self.board = toggle_square(self.board, square_id)

        if self.winning_line is None:
            bingo = check_bingo(self.board)
            if bingo is not None:
                self.winning_line = bingo
                self.game_state = GameState.BINGO
                self.show_bingo_modal = True

    def reset_game(self) -> None:
        self.game_state = GameState.START
        self.board = []
        self.winning_line = None
        self.show_bingo_modal = False
        self.quiz_errors = []
        self.pending_custom_input = ""
        self.used_custom_questions = False

    def dismiss_modal(self) -> None:
        self.show_bingo_modal = False
        self.game_state = GameState.PLAYING


# In-memory session store keyed by session ID
_sessions: dict[str, GameSession] = {}


def get_session(session_id: str) -> GameSession:
    """Get or create a game session for the given session ID."""
    if session_id not in _sessions:
        _sessions[session_id] = GameSession()
    return _sessions[session_id]
