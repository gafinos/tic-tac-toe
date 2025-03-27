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

def get_move(player: str) -> int:
    """Prompt player for move input and validate it.
    Ask for new input if invalid value is passed.
    
    Args:
        player (str): Symbol of the player
    Returns:
        int: The number marking the field of the move
    """
    
    while True:
        move = input(f"Player {player} | Enter your move number: ")
        if move == "q":
            sys.exit()
        elif str.isnumeric(move):
            if int(move) not in range(1,10):
                print("Wrong field number. Please enter a number from 1 to 9. Press q to quit the game.")
            else:
                return int(move)
        else:
            print("Invalid input. Please enter a number from 1 to 9. Press q to quit the game.")

def draw_board(board: list) -> None:
    """Prints the current board state.
    
    Args:
        board (list): 2D list of 3x3 tic-tac-toe board field values"""
    
    separator = '+---+---+---+'
    print(separator)
    for     row in board:
        print('| {} | {} | {} |'.format(*row),separator,sep="\n")

def check_player_win(board: list, player: str) -> bool:
    """Check player symbol horizontally, vertically, and diagonally to evaluate win.
    Args:
        board (list): 2D list of 3x3 tic-tac-toe board field values
        player (str): Symbol of the player to evalute"""
    
    # count vertical
    for row in board:
        win = list.count(row,player) == 3

    #count horizontal
    for index in board[0]:
        column = [row[index] for row in board]
        win = list.count(column,player) == 3

    #count diagonals
    diagonal_desc = [board[0][0],board[1][1],board[2][2]]
    diagonal_asc = [board[2][0],board[1][1],board[0][2]]

def update_board(board: list, player: str, move: int) -> list:
    """Update board based on the player's move.
    
    Args:
        board (list): 2D list of 3x3 tic-tac-toe board field values
        player (str): Symbol of the player
        move (int): Numeric representation of the field to update (1-9)
    Returns:
        list: 2D list of 3x3 tic-tac-toe board field values"""
    
    board[(move - 1) // 3][(move - 1) % 3] = player
    return board


winner = None

draw_board(board)
while winner is None:
    for player in VALID_PLAYERS:
        move = get_move(player)
        update_board(board,player,move)
        draw_board(board)
        # if check_player_win(board,player):
        #     winner = player