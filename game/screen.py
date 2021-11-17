from rich.console import Console
from rich.prompt import IntPrompt
from .board import Board

from typing import Optional


class Screen:
    def __init__(self):
        self.board = Board()
        self.console = Console()

    def turn(self) -> Optional[int]:
        self.print_screen()
        move = IntPrompt.ask("Which column do you want to put your piece in?\n", choices=list(map(str, range(7))))
        try:
            return self.board.add_move(move)
        except ValueError as e:
            print(e)
            return None

    def print_screen(self) -> None:
        self.console.rule("Connect 4 Game", style="#FF00FF")
        print("\n")
        self.print_board()
        print("\n" * (self.console.size.height - 12))

    def print_board(self) -> None:
        for x in reversed(self.board.grid):
            self.console.print(" ".join(self.f(y) for y in x), justify="center")

    @staticmethod
    def f(n: int) -> str:
        if n == 0:
            return "0"
        elif n == 1:
            return "[red]0[/red]"
        else:
            return "[#FFFB03]0[/#FFFB03]"
