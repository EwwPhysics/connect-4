from .screen import Screen

game = Screen()

while True:
    t = game.turn()
    
    if t is not None:
        game.print_screen(finished=True)
        break
