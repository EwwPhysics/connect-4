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

    assert b._grid[0, 3] == 1


def test_switch_turn():
    b = board.Board()
    b.add_move(3)

    assert b.turn == -1


def test_win_vertical():
    # Board state to test
    # x
    # x o
    # x o
    # x o

    b = board.Board()
    for _ in range(3):
        b.add_move(0)
        b.add_move(1)

    b.add_move(0)

    print(b._grid)

    assert b._check_win()


def test_win_horizontal():
    # Board state to test
    # o o o
    # x x x x

    b = board.Board()
    for i in range(3):
        b.add_move(i)
        b.add_move(i)

    b.add_move(3)
    print(b._grid)

    assert b._check_win()


def test_win_diagonal():
    # Board state to test
    #       x
    #     x o
    # o x x x
    # x o o o

    b = board.Board()
    b.add_move(0)
    b.add_move(1)
    b.add_move(1)
    b.add_move(2)
    b.add_move(2)
    b.add_move(3)
    b.add_move(2)
    b.add_move(0)
    b.add_move(3)
    b.add_move(3)
    b.add_move(3)

    assert b._check_win()
