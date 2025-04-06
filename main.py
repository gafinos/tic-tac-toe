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

max_turns = board[0].count(' ') ** 2
h_line = 40 * '='

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
        if list.count(row,player) == 3:
            return True
    #count vertical
    for index in range(0,3):
        column = [board[0][index],board[1][index],board[2][index]]
        if list.count(column,player) == 3:
            return True
    #count diagonals
    diagonal_desc = [board[0][0],board[1][1],board[2][2]]
    diagonal_asc = [board[2][0],board[1][1],board[0][2]]
    if list.count(diagonal_asc,player) == 3 or list.count(diagonal_desc,player) == 3:
        return True
    
def update_board(board: list, player: str, move: int) -> list:
    """Update board based on the player's move. Returns None if field is not available.
    
    Args:
        board (list): 2D list of 3x3 tic-tac-toe board field values
        player (str): Symbol of the player
        move (int): Numeric representation of the field to update (1-9)
    Returns:
        list: 2D list of 3x3 tic-tac-toe board field values"""
    if board[(move - 1) // 3][(move - 1) % 3] == " ":
        board[(move - 1) // 3][(move - 1) % 3] = player
        return board
    else:
        print("The field is already taken, try again.")
    

winner = None
turn_counter = 0
# WELCOME
print(welcome_text)
print(40 * "-")
draw_board(board)

# GAME LOOP
while True:
    for player in VALID_PLAYERS:
        turn_counter += 1
        while turn_counter <= max_turns: # Skipping round if all fields are filled
            print(h_line)
            move = get_move(player)
            if update_board(board,player,move) is None: # Keep asking user for input if not valid
                continue
            else:
                break
        print(h_line)
        draw_board(board)
        if check_player_win(board,player):
            print(f"Congratulations, the player {player} WON!")
            sys.exit()
        elif turn_counter >= max_turns: # All fields are filled
            print("It's a tie!")
            sys.exit()