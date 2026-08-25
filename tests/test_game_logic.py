from app.data import FREE_SPACE, MAX_QUESTION_LENGTH, QUESTIONS, REQUIRED_QUESTION_COUNT
from app.game_logic import (
    CENTER_INDEX,
    check_bingo,
    generate_board,
    get_winning_square_ids,
    parse_custom_questions,
    toggle_square,
    validate_questions,
)
from app.models import BingoLine, BingoSquareData


class TestGenerateBoard:
    def test_board_has_25_squares(self):
        board = generate_board()
        assert len(board) == 25

    def test_center_is_free_space(self):
        board = generate_board()
        center = board[CENTER_INDEX]
        assert center.is_free_space is True
        assert center.is_marked is True
        assert center.text == FREE_SPACE

    def test_non_center_squares_are_not_free_space(self):
        board = generate_board()
        for i, square in enumerate(board):
            if i != CENTER_INDEX:
                assert square.is_free_space is False
                assert square.is_marked is False

    def test_all_questions_from_pool(self):
        board = generate_board()
        texts = {s.text for s in board if not s.is_free_space}
        assert texts.issubset(set(QUESTIONS))

    def test_squares_have_sequential_ids(self):
        board = generate_board()
        for i, square in enumerate(board):
            assert square.id == i

    def test_board_is_shuffled(self):
        """Verify two boards aren't identical (high probability)."""
        board1 = generate_board()
        board2 = generate_board()
        texts1 = [s.text for s in board1]
        texts2 = [s.text for s in board2]
        # Extremely unlikely to be identical
        assert texts1 != texts2


class TestToggleSquare:
    def test_toggle_marks_unmarked_square(self):
        board = generate_board()
        square_id = 0
        assert board[square_id].is_marked is False
        new_board = toggle_square(board, square_id)
        assert new_board[square_id].is_marked is True

    def test_toggle_unmarks_marked_square(self):
        board = generate_board()
        board = toggle_square(board, 0)
        assert board[0].is_marked is True
        board = toggle_square(board, 0)
        assert board[0].is_marked is False

    def test_toggle_does_not_affect_free_space(self):
        board = generate_board()
        new_board = toggle_square(board, CENTER_INDEX)
        assert new_board[CENTER_INDEX].is_marked is True  # Still marked

    def test_toggle_returns_new_list(self):
        board = generate_board()
        new_board = toggle_square(board, 0)
        assert board is not new_board


class TestCheckBingo:
    def _make_board(self, marked_ids: set[int]) -> list[BingoSquareData]:
        board = generate_board()
        result = []
        for square in board:
            if square.id in marked_ids or square.is_free_space:
                result.append(
                    BingoSquareData(
                        id=square.id,
                        text=square.text,
                        is_marked=True,
                        is_free_space=square.is_free_space,
                    )
                )
            else:
                result.append(square)
        return result

    def test_no_bingo_initially(self):
        board = generate_board()
        assert check_bingo(board) is None

    def test_row_bingo(self):
        # Mark first row: indices 0-4
        board = self._make_board({0, 1, 2, 3, 4})
        result = check_bingo(board)
        assert result is not None
        assert result.type == "row"
        assert result.squares == [0, 1, 2, 3, 4]

    def test_column_bingo(self):
        # Mark first column: indices 0, 5, 10, 15, 20
        board = self._make_board({0, 5, 10, 15, 20})
        result = check_bingo(board)
        assert result is not None
        assert result.type == "column"
        assert result.squares == [0, 5, 10, 15, 20]

    def test_diagonal_bingo(self):
        # Mark diagonal: 0, 6, 12, 18, 24 (12 is free space)
        board = self._make_board({0, 6, 18, 24})
        result = check_bingo(board)
        assert result is not None
        assert result.type == "diagonal"
        assert result.squares == [0, 6, 12, 18, 24]

    def test_partial_line_no_bingo(self):
        board = self._make_board({0, 1, 2, 3})  # Only 4 of 5 in first row
        assert check_bingo(board) is None


class TestGetWinningSquareIds:
    def test_none_line_returns_empty_set(self):
        assert get_winning_square_ids(None) == set()

    def test_returns_square_ids(self):
        line = BingoLine(type="row", index=0, squares=[0, 1, 2, 3, 4])
        assert get_winning_square_ids(line) == {0, 1, 2, 3, 4}


class TestParseCustomQuestions:
    def test_splits_on_newlines_and_strips_whitespace(self):
        raw = "  question one  \nquestion two\n"
        assert parse_custom_questions(raw) == ["question one", "question two"]

    def test_drops_blank_lines(self):
        raw = "question one\n\n   \nquestion two"
        assert parse_custom_questions(raw) == ["question one", "question two"]

    def test_deduplicates_case_insensitively_preserving_first_occurrence(self):
        raw = "Loves Pizza\nloves pizza\nLOVES PIZZA\nhas a dog"
        assert parse_custom_questions(raw) == ["Loves Pizza", "has a dog"]

    def test_empty_input_returns_empty_list(self):
        assert parse_custom_questions("") == []
        assert parse_custom_questions("   \n  \n") == []


class TestValidateQuestions:
    def test_valid_questions_return_no_errors(self):
        questions = [
            f"custom question number {i}" for i in range(REQUIRED_QUESTION_COUNT)
        ]
        assert validate_questions(questions) == []

    def test_too_few_questions_returns_error(self):
        questions = ["only one question"]
        errors = validate_questions(questions)
        assert len(errors) == 1
        assert "at least" in errors[0]

    def test_question_too_short_returns_error(self):
        questions = [f"q{i}" for i in range(REQUIRED_QUESTION_COUNT)]
        questions[0] = "ab"
        errors = validate_questions(questions)
        assert any("characters long" in e and "at least" in e for e in errors)

    def test_question_too_long_returns_error(self):
        questions = [
            f"custom question number {i}" for i in range(REQUIRED_QUESTION_COUNT)
        ]
        questions[0] = "x" * (MAX_QUESTION_LENGTH + 1)
        errors = validate_questions(questions)
        assert any("at most" in e for e in errors)

    def test_empty_list_returns_count_error_only(self):
        errors = validate_questions([])
        assert len(errors) == 1


class TestGenerateBoardWithCustomQuestions:
    def test_uses_custom_question_pool(self):
        custom = [f"custom question {i}" for i in range(REQUIRED_QUESTION_COUNT)]
        board = generate_board(custom)
        texts = {s.text for s in board if not s.is_free_space}
        assert texts.issubset(set(custom))
        assert not texts.issubset(set(QUESTIONS))

    def test_board_still_has_25_squares_and_free_space(self):
        custom = [f"custom question {i}" for i in range(REQUIRED_QUESTION_COUNT)]
        board = generate_board(custom)
        assert len(board) == 25
        assert board[CENTER_INDEX].is_free_space is True

    def test_none_falls_back_to_default_pool(self):
        board = generate_board(None)
        texts = {s.text for s in board if not s.is_free_space}
        assert texts.issubset(set(QUESTIONS))

    def test_empty_list_falls_back_to_default_pool(self):
        board = generate_board([])
        texts = {s.text for s in board if not s.is_free_space}
        assert texts.issubset(set(QUESTIONS))
