import os

from helpers import draw_board, check_turn, check_for_win

# algorithm, key:data
spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
         6: '6', 7: '7', 8: '8', 9: '9'}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    # reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    # if an invalid turn ocurred, let the player know
    if prev_turn == turn:
        print("Número invalido, seleccione un número de la tabla.")
        prev_turn = turn
    print("Player" + str((turn % 2) + 1) + "'s turno: Elige un número de la tabla"
                                           " o presiona 'q' para salir")
    # get input from the player
    choice = input()
    if choice == 'q':
        playing = False
        print("T...")
    # check if the player gave a number from 1-9
    elif str.isdigit(choice) and int(choice) in spots:
        # Check if the spot has already been taken
        if not spots[int(choice)] in {"X", "O"}:
            # Valid input, update the board
            turn += 1
            spots[int(choice)] = check_turn(turn)
            # if the game has ended (and if someone won)
    if check_for_win(spots): playing, complete = False, True
    if turn > 8: playing = False
# out of loop, print the result
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
# If there was a winner, say who won
if complete:
    if check_turn(turn) == 'X':
        print("Player 1 Wins")
    else:
        print("Player 2 Wins")
else:
    # Tie game
    print("No hay ganador.")

print("Gracias por jugar.")
