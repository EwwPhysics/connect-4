from .screen import Screen

game = Screen()

while True:
    t = game.turn()
    
    if t is not None:
        game.print_board()
        print()
        
        game.console.print(
            ":partying_face::pleading_face::weary_face: Player",
            "1" if t == 1 else "2",
            "won :partying_face::pleading_face::weary_face:",
            justify="center",
            style="bold red",
        )
        break
