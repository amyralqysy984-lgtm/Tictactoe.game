"""
Tic-Tac-Toe Game Project
Implementation of Python Fundamentals:
- 2D Lists
- Functions & Game Logic
- Loops & Conditionals
- Input Validation
- Random Module
"""

from random import randrange

# 1. Display the board in a clean, formatted grid layout
def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

# 2. Handle user move ('O') with input validation
def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input! Please choose a number between 1 and 9.")
                continue
            
            row = (move - 1) // 3
            col = (move - 1) % 3
            
            if type(board[row][col]) == int:
                board[row][col] = 'O'
                break
            else:
                print("That square is already taken! Try another one.")
        except ValueError:
            print("Please enter a valid integer number!")

# 3. Handle computer move ('X') using random choices from available squares
def draw_move(board):
    free_squares = []
    for row in range(3):
        for col in range(3):
            if type(board[row][col]) == int:
                free_squares.append((row, col))
                
    if free_squares:
        rw, cl = free_squares[randrange(len(free_squares))]
        board[rw][cl] = 'X'

# 4. Check for victory or tie conditions
def check_victory(board, sign):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True
    # Check diagonals
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False

# 5. Main game execution loop
if __name__ == "__main__":
    board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
    
    print("--- Welcome to Tic-Tac-Toe Game ---")
    
    while True:
        display_board(board)
        
        # Player's turn
        enter_move(board)
        if check_victory(board, 'O'):
            display_board(board)
            print("Congratulations! You won!")
            break
            
        # Computer's turn
        draw_move(board)
        if check_victory(board, 'X'):
            display_board(board)
            print("Computer wins! Better luck next time.")
            break

