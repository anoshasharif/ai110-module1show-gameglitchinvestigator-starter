import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from logic_utils import check_guess


def test_guess_above_secret_returns_too_high():
    outcome, _message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_below_secret_returns_too_low():
    outcome, _message = check_guess(40, 50)
    assert outcome == "Too Low"