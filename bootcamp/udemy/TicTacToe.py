from IPython.display import clear_output
import random


def printLine(board):
    print('|', end = '')
    for input in board:
        print(' ' + input + ' |', end = '')
    print()

def display_board(board):
    clear_output()
    for x in range(1,8,3):
        printLine(board[x:x+3])

def player_input():
    player1 = input("Please pick a marker 'X' or 'O'")
    return player1

def place_marker(board, marker, position):
    board[position] = marker


def same(board, mark):
    return board.count(board[0]) == len(board)

def win_check(board, mark):
    for x in range(1, 8, 3):
        if same(board[x:x + 3], mark):
            return True

    for x in range(1, 4):
        if same(board[x:x + 6:3], mark):
            return True

    for x in range(1, 4):
        if (board[1] == mark and board[5] == mark and board[9] == mark) or (
                board[3] == mark and board[5] == mark and board[7] == mark):
            return True

    return False

def choose_first():
    if random.randint(10) > random.randint(10):
        return True
    else:
        return False

def space_check(board, position):
    if board[position] != 'X' and board[position] != 'O':
        return True
    else:
        return False


def full_board_check(board):
    for spot in range(1, 10):
        if space_check(board, spot):
            return False

    return True

def player_choice(board):
    position = int(input('Please enter a number'))
    if space_check(board, position):
        return position
    else:
        return -1

def replay():
    player1 = input("Again? yes or no")
    if player1 == 'yes':
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
