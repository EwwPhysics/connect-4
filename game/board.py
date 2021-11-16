import numpy as np
from scipy.signal import convolve, convolve2d

from typing import Optional


FLAT = np.ones((1, 4), dtype=np.byte)
DIAG = np.array(
    [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ],
    dtype=np.byte,
)


class Board:
    """
    Maintains the board state of the game.

    Attributes:
        turn: An int, either -1 or 1, that keeps track of whose turn it is
    """

    def __init__(self):
        self._grid = np.zeros((6, 7), dtype=np.byte)

        self.turn = 1

    def add_move(self, col: int) -> Optional[int]:
        """
        Given a column, try to insert a piece at that column.

        If adding the piece does not result in a win, update the `turn` attribute
        to switch turns.

        Args:
            col: The column to try to insert a piece at. Valid values are in the range 0 <= col < 7.

        Returns:
            If a player has won, return `self.turn`. Otherwise, return None

        Raises:
            ValueError: The specified column was full.
        """

        if col < 0 or col > 6:
            raise ValueError(f"Column must be in the range 0 <= col < 7")

        row = len(self._grid[:, col].nonzero()[0])

        if row == 6:
            raise ValueError(f"Column {col} is full")

        self._grid[row, col] = self.turn

        if self._check_win():
            return self.turn

        self.turn *= -1

        return None

    def _check_win(self) -> bool:
        """
        Check if there is a 4-in-a-row in the grid.

        Returns:
            True if there is a 4-in-a-row, false otherwise.
        """

        horizontal = convolve2d(self._grid, FLAT)
        if abs(horizontal).max() >= 4:
            return True

        vertical = convolve2d(self._grid, np.rot90(FLAT))
        if abs(vertical).max() >= 4:
            return True

        diag = convolve(self._grid, DIAG)
        if abs(diag).max() >= 4:
            return True

        diag = convolve(self._grid, np.rot90(DIAG))
        if abs(diag).max() >= 4:
            return True

        return False
    
    @property
    def grid(self):
        return self._grid

