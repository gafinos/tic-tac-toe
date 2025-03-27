"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Václav Špaček
email: gafinos@gmail.com
"""
import sys

VALID_PLAYERS = ["X","O"]
welcome_text = """Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game"""

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def prompt_player(player):
    """Prompt player for move input and validate it.
    Ask for new input if invalid value is passed.
    
    Args:
        player (str): Symbol of the player - either X or O
    Returns:
        int: The number marking the field of the move
    """
    if player not in VALID_PLAYERS:
        print("Invalid player")
        sys.exit()
    
    while True:
        move = input(f"Player {player} | Enter your move number: ")
        if move == "q":
            sys.exit()
        elif str.isnumeric(move):
            if int(move) not in range(1,10):
                print("Wrong field number. Please enter a number from 1 to 9. Press q to quit the game.")
            else:
                break
        else:
            print("Invalid input. Please enter a number from 1 to 9. Press q to quit the game.")

def draw_board(board):
    """Prints the current board state."""
    pass

def check_player_win(board, player):
    """Check player symbol horizontally, vertically, and diagonally to evaluate win."""
    # count vertical
    for row in board:
        win = list.count(row,player) == 3

    #count horizontal
    for index in board[0]:
        column = [row[index] for row in board]
        win = list.count(column,player) == 3

    #count diagonal
    diagonal_desc = [board[0][0],board[1][1],board[2][2]]
    diagonal_asc = [board[2][0],board[1][1],board[0][2]]

while winner is None:
    for player in VALID_PLAYERS:
        draw_board(board)
        prompt_player(player)
        if check_player_win(board,player):
            winner = player
