def draw_board(spots):
    # metodo que muestra la tabla
 board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
             f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
             f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    # F string syntax:
    # I'm a string {I'm a variable} I'm another variable...
 print(board)


def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'


def check_for_win(spots):
    # horizontal cases
    if (spots[1] == spots[2] == spots[3]) \
            or (spots[4] == spots[5] == spots[6]) \
            or (spots[7] == spots[8] == spots[9]):
        return True
    # Vertical cases
    elif (spots[1] == spots[4] == spots[7]) \
            or (spots[2] == spots[5] == spots[8]) \
            or (spots[3] == spots[6] == spots[9]):
        return True
    # Diagonal Cases
    elif (spots[1] == spots[5] == spots[9]) \
            or (spots[3] == spots[5] == spots[7]):
        return True

    else:
        return False
