from IPython.display import clear_output
import random


def print_line(gameboard):
    print('|', end='')
    for spot in gameboard:
        print(' ' + spot + ' |', end='')
    print()


def display_board(gameboard):
    clear_output()
    for x in range(1, 8, 3):
        print_line(gameboard[x:x + 3])


def player_input():
    player1 = input("Please pick a marker 'X' or 'O'")
    return player1


def place_marker(gameboard, marker, pos):
    gameboard[pos] = marker


def same(gameboard, mark):
    return gameboard.count(mark) == len(gameboard)


def win_check(gameboard, mark):
    for x in range(1, 8, 3):
        if same(gameboard[x:x + 3], mark):
            return True

    for x in range(1, 4):
        if same(gameboard[x:x + 6:3], mark):
            return True

    for x in range(1, 4):
        if (gameboard[1] == mark and gameboard[5] == mark and gameboard[9] == mark) or (
                gameboard[3] == mark and gameboard[5] == mark and gameboard[7] == mark):
            return True

    return False


def choose_first():
    if random.randint(10) > random.randint(10):
        return True
    else:
        return False


def space_check(gameboard, pos):
    if gameboard[pos] != 'X' and gameboard[pos] != 'O':
        return True
    else:
        return False


def full_board_check(gameboard):
    for spot in range(1, 10):
        if space_check(gameboard, spot):
            return False

    return True


def player_choice(gameboard):
    pos = int(input('Please enter a number'))
    if space_check(gameboard, pos):
        return pos
    else:
        return -1


def replay():
    answer = input("Again? yes or no")
    if answer == 'yes':
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')
board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display_board(board)

while True:
    # Set the game up here
    player1 = player_input()

    game_on = True
    while game_on:
        # Player 1 Turn
        if full_board_check(board):
            break

        position = -1
        while position == -1:
            position = player_choice(board)

        place_marker(board, 'X', position)
        display_board(board)
        if win_check(board, 'X'):
            print('Player 1 won')
            break
        # Player2's turn.
        if full_board_check(board):
            break

        position = -1
        while position == -1:
            position = player_choice(board)

        place_marker(board, 'O', position)
        display_board(board)
        if win_check(board, 'O'):
            print('Player 2 won')
            break
            # pass

    if not replay():
        break
