from ascii_art import logo
from positions import Positions

print(logo)
print("A game of Tic Tac Toe between Player X and Player O")
print("Simply enter the game-board position during each player's turn\n")

while True:

    start = input("Enter 'Y' to play or 'E' to exit: ").upper()

    if start == "Y":
        positions = Positions()
        positions.game_board()

        for turn_number in range(9):
            if turn_number % 2 == 0:
                positions.player_move('X')
            else:
                positions.player_move('O')
            if positions.winner():
                break
        if not positions.winner():
            print("Game ended in a draw")
    elif start == "E":
        print("Game ended")
        break
    else:
        print("Not valid input")



