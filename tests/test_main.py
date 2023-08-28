"""Test cases for the __main__ module."""
import pytest
from click.testing import CliRunner
from pytest_mock import MockerFixture

from german_grammar import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner, mocker: MockerFixture) -> None:
    """It exits with a status code of zero."""
    mocker.patch("german_grammar.__main__.get_exercise_count", return_value=1)
    mocker.patch("german_grammar.__main__.get_answer", return_value="das Kind")
    result = runner.invoke(__main__.main)
    assert result.exit_code == 0
