import pytest
from fastapi.testclient import TestClient

from app.data import REQUIRED_QUESTION_COUNT
from app.main import app


@pytest.fixture
def client():
    return TestClient(app)


class TestHomePage:
    def test_home_returns_200(self, client: TestClient):
        response = client.get("/")
        assert response.status_code == 200

    def test_home_contains_start_screen(self, client: TestClient):
        response = client.get("/")
        assert "Soc Ops" in response.text
        assert "Start Game" in response.text
        assert "How to play" in response.text

    def test_home_sets_session_cookie(self, client: TestClient):
        response = client.get("/")
        assert "session" in response.cookies


class TestStartGame:
    def test_start_returns_game_board(self, client: TestClient):
        # First visit to get session
        client.get("/")
        response = client.post("/start")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text
        assert "← Back" in response.text

    def test_board_has_25_squares(self, client: TestClient):
        client.get("/")
        response = client.post("/start")
        # Count the toggle buttons (squares with hx-post="/toggle/")
        assert response.text.count('hx-post="/toggle/') == 24  # 24 + 1 free space


class TestToggleSquare:
    def test_toggle_marks_square(self, client: TestClient):
        client.get("/")
        client.post("/start")
        response = client.post("/toggle/0")
        assert response.status_code == 200
        # The response should contain the game screen with a marked square
        assert "FREE SPACE" in response.text


class TestResetGame:
    def test_reset_returns_start_screen(self, client: TestClient):
        client.get("/")
        client.post("/start")
        response = client.post("/reset")
        assert response.status_code == 200
        assert "Start Game" in response.text
        assert "How to play" in response.text


class TestDismissModal:
    def test_dismiss_returns_game_screen(self, client: TestClient):
        client.get("/")
        client.post("/start")
        response = client.post("/dismiss-modal")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text


class TestCustomizeQuiz:
    def test_customize_returns_customize_screen(self, client: TestClient):
        client.get("/")
        response = client.get("/customize")
        assert response.status_code == 200
        assert "Custom" in response.text
        assert "Start with My Questions" in response.text

    def test_start_with_valid_custom_questions_uses_them(self, client: TestClient):
        client.get("/")
        custom_questions = "\n".join(
            f"custom question {i}" for i in range(REQUIRED_QUESTION_COUNT)
        )
        response = client.post("/start", data={"custom_questions": custom_questions})
        assert response.status_code == 200
        assert "custom question 0" in response.text
        assert "FREE SPACE" in response.text
        assert "CUSTOM QUIZ" in response.text

    def test_start_with_too_few_custom_questions_shows_errors(
        self, client: TestClient
    ):
        client.get("/")
        response = client.post(
            "/start", data={"custom_questions": "only one question"}
        )
        assert response.status_code == 200
        assert "Start with My Questions" in response.text  # back on customize screen
        assert "at least" in response.text
        assert "only one question" in response.text  # preserves user's input

    def test_start_with_malformed_whitespace_only_falls_back_to_default(
        self, client: TestClient
    ):
        client.get("/")
        response = client.post("/start", data={"custom_questions": "   \n\n  "})
        assert response.status_code == 200
        assert "← Back" in response.text
        assert "FREE SPACE" in response.text
        assert "CUSTOM QUIZ" not in response.text

    def test_start_without_custom_questions_is_backward_compatible(
        self, client: TestClient
    ):
        client.get("/")
        response = client.post("/start")
        assert response.status_code == 200
        assert "FREE SPACE" in response.text
        assert "← Back" in response.text
        assert "CUSTOM QUIZ" not in response.text

    def test_use_default_button_ignores_pending_custom_input(
        self, client: TestClient
    ):
        client.get("/")
        client.get("/customize")
        response = client.post("/start", data={"custom_questions": ""})
        assert response.status_code == 200
        assert "FREE SPACE" in response.text
        assert "CUSTOM QUIZ" not in response.text

    def test_reset_clears_custom_quiz_state(self, client: TestClient):
        client.get("/")
        custom_questions = "\n".join(
            f"custom question {i}" for i in range(REQUIRED_QUESTION_COUNT)
        )
        client.post("/start", data={"custom_questions": custom_questions})
        response = client.post("/reset")
        assert response.status_code == 200
        assert "Start Game" in response.text
        # Starting again without customization should use the default bank.
        follow_up = client.post("/start")
        assert "custom question 0" not in follow_up.text
        assert "CUSTOM QUIZ" not in follow_up.text
