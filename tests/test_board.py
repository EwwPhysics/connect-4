import pytest

from game import board


def test_out_of_range_column():
    b = board.Board()
    with pytest.raises(ValueError):
        b.add_move(10)


def test_full_column():
    b = board.Board()

    for _ in range(6):
        b.add_move(3)

    with pytest.raises(ValueError):
        b.add_move(3)


def test_board_add():
    b = board.Board()
    b.add_move(3)

    assert b.grid[0, 3] == 1


def test_switch_turn():
    b = board.Board()
    b.add_move(3)

    assert b.turn == -1
