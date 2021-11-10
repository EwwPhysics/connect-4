import numpy as np


class Board:
    """
    Maintains the board state of the game.

    Attributes:
        grid: A numpy array containing the board state
        turn: An int, either -1 or 1, that keeps track of whose turn it is
    """

    def __init__(self):
        self.grid = np.zeros((6, 7), dtype=np.byte)

        self.turn = 1

    def add_move(self, col: int) -> bool:
        """
        Given a column, try to insert a piece at that column.

        Args:
            col: The column to try to insert a piece at

        Returns:
            True if by inserting the piece, the player has won. False otherwise

        Raises:
            ValueError: The column was out of bounds, or the column was full.
        """

        if col < 0 or col > 6:
            raise ValueError(f"Column must be in the range 0 <= col < 7")

        row = len(self.grid[:, col].nonzero()[0])

        # TODO: Check if the column is full

        self.grid[row, col] = self.turn

        # TODO: Check if the player has won after inserting this piece

        self.turn *= -1

        return False

    def _check_win(self, row: int, col: int) -> bool:
        """
        Check if there is a 4-in-a-row that includes the point (row, col).

        Args:
            row: The row of the point
            col: The column of the point

        Returns:
            True if there is a 4-in-a-row, false otherwise.
        """

        pass
