import pytest

from game import board


def test_board_raises():
    b = board.Board()
    with pytest.raises(ValueError):
        b.add_move(10)
