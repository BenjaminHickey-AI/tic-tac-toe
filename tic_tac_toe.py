import random

# Initialize empty 3x3 board
def init_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Display the board
def print_board(board):
    print("\n  0   1   2")
    for i, row in enumerate(board):
        print(i, ' | '.join(row))
        if i < 2:
            print("  ---------")
    print()

# Check if a player has won
def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)): return True
        if all(board[j][i] == player for j in range(3)): return True
    if all(board[i][i] == player for i in range(3)): return True
    if all(board[i][2 - i] == player for i in range(3)): return True
    return False

# Check for tie
def check_tie(board):
    return all(cell != ' ' for row in board for cell in row)

# Get all empty cells
def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

# AI rules with move coordinates
def ai_move(board):
    # Rule 1: Win if possible
    for i, j in get_empty_cells(board):
        board[i][j] = 'X'
        if check_win(board, 'X'):
            print(f"AI's move: ({i}, {j})")
            return
        board[i][j] = ' '

    # Rule 2: Block opponent
    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        if check_win(board, 'O'):
            board[i][j] = 'X'
            print(f"AI's move: ({i}, {j})")
            return
        board[i][j] = ' '

    # Rule 3: Take center
    if board[1][1] == ' ':
        board[1][1] = 'X'
        print("AI's move: (1, 1)")
        return

    # Rule 4: Take opposite corner
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    opposite = {(0, 0): (2, 2), (0, 2): (2, 0), (2, 0): (0, 2), (2, 2): (0, 0)}
    for corner in corners:
        i, j = corner
        if board[i][j] == 'O':
            oi, oj = opposite[corner]
            if board[oi][oj] == ' ':
                board[oi][oj] = 'X'
                print(f"AI's move: ({oi}, {oj})")
                return

    # Rule 5: Take any empty corner
    for i, j in corners:
        if board[i][j] == ' ':
            board[i][j] = 'X'
            print(f"AI's move: ({i}, {j})")
            return

    # Rule 6: Take any side
    sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
    for i, j in sides:
        if board[i][j] == ' ':
            board[i][j] = 'X'
            print(f"AI's move: ({i}, {j})")
            return

# Human move input
def human_move(board):
    while True:
        try:
            move = input("Enter your move (row col): ").split()
            if len(move) != 2:
                raise ValueError
            row, col = map(int, move)
            if board[row][col] == ' ':
                board[row][col] = 'O'
                break
            else:
                print("That cell is taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter row and column (0-2).")

# Main game loop with first-move option
def play_game():
    board = init_board()
    print("Welcome to Tic-Tac-Toe! You are O, AI is X.")

    # First move choice
    while True:
        first = input("Who goes first? (human/ai): ").strip().lower()
        if first in ('human', 'ai'):
            break
        print("Invalid choice. Type 'human' or 'ai'.")

    print_board(board)

    current = 'human' if first == 'human' else 'ai'

    while True:
        if current == 'human':
            human_move(board)
            print_board(board)
            if check_win(board, 'O'):
                print("You win!")
                break
            current = 'ai'
        else:
            ai_move(board)
            print_board(board)
            if check_win(board, 'X'):
                print("AI wins!")
                break
            current = 'human'

        if check_tie(board):
            print("It's a tie!")
            break

# Run the game
if __name__ == "__main__":
    play_game()

