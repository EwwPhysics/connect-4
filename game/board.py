import numpy as np
from scipy.signal import convolve

from typing import Optional


KERNEL = np.ones((4, 4), dtype=np.byte)


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
            col: The column to try to insert a piece at

        Returns:
            If a player has won, return `self.turn`
            Otherwise, return None

        Raises:
            ValueError: The column was out of bounds, or the column was full.
        """

        if col < 0 or col > 6:
            raise ValueError(f"Column must be in the range 0 <= col < 7")

        row = len(self._grid[:, col].nonzero()[0])

        # TODO: Check if the column is full

        self._grid[row, col] = self.turn

        if self._check_win():
            return self.turn

        self.turn *= -1

        return None

    def _check_win(self) -> bool:
        """
        Check if there is a 4-in-a-row that includes the point (row, col).

        Returns:
            True if there is a 4-in-a-row, false otherwise.
        """

        neighbors = convolve(self._grid, KERNEL)

        return abs(neighbors).max() >= 4
