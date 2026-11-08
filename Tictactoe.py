"""
Tic-Tac-Toe Game Project
Implementation of Python Fundamentals:
- 2D Lists
- Functions
- Loops & Conditionals
- Random Module
"""

from random import randrange

# 1. Initialize the board (3x3 grid with 'X' in the center)
board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
]

# 2. Display the board
def display_board(board):
    print(board[0])
    print(board[1])
    print(board[2])

# 3. Handle user move ('O')
def enter_move(board):
    move = int(input("Enter square number (1-9): "))
    for row in range(3):
        for col in range(3):
            if board[row][col] == move:
                board[row][col] = 'O'
                return True
    return False

# 4. Handle computer move ('X')
def draw_move(board):
    while True:
        square = randrange(9)
        row = square // 3
        col = square % 3
        if type(board[row][col]) == int:
            board[row][col] = 'X'
            break

# 5. Game execution
if __name__ == "__main__":
    print("--- Tic-Tac-Toe Game ---")
    display_board(board)
    
    enter_move(board)
    display_board(board)
    
    draw_move(board)
    print("Computer move:")
    display_board(board)
