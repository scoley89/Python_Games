# ____________ Globals ________________

game_continues = True
winner = None
current_player = "X"


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def display_win():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    display_win()
    while game_continues:
        handle_flip(current_player)
        if_game_over()
        flip_player()
        # the game has ended
        if winner == "X" or winner == "O":
            print(winner + " won.")
        elif winner == None:
            print("Sorry no winner!")


def handle_flip(player):
    print(player + "'s turn!")
    position = input("Choose a position from 1 - 9: ")

    valid = False

    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input(
                "We don´t take that stuff around here. Try a number! 1-9 ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Nice try you sly Fox but that don´t fly around here!")

    board[position] = player
    display_win()


def if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner

    row_winner = check_rows()
    columbs_winner = check_columbs()
    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif columbs_winner:
        winner = columbs_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return()


def check_rows():
    global game_continues
    # check if rows share values or not
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any row is a match show that there is a win
    if row_1 or row_2 or row_3:
        game_continues = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columbs():
    global game_continues
    # check if col share values or not
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    # if any col is a match show that there is a win
    if col_1 or col_2 or col_3:
        game_continues = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonals():
    global game_continues
    # check if diag share values or not
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"

    # if any col is a match show that there is a win
    if diag_1 or diag_2:
        game_continues = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    return


def check_if_tie():
    global game_continues
    if "-" not in board:
        game_continues = False
    return


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
        return
    return


play_game()


# The Plan of Attack
# make board
# check win
# check tie
# player flip
# display board
# play game
