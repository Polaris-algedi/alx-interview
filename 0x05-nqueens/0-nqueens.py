#!/usr/bin/python3


import sys


def is_safe(board, row, col):
    """Checks if a queen can be placed at the given row and column."""
    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Check lower diagonal on right side
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True


def solve_n_queens(board, col):
    """Solves the N-queens problem using backtracking."""
    if col >= len(board):
        # All queens placed, print the solution
        solution = []
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == 1:
                    solution.append([row, col])
        print(solution)
        return

    # Try placing queen in all possible rows of current column
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens(board, col + 1)
            board[row][col] = 0  # Backtrack


def main():
    """Main function to handle program execution."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    if n < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    # Initialize empty chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Solve the N-queens problem
    solve_n_queens(board, 0)


if __name__ == "__main__":
    main()
