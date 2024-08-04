#!/usr/bin/python3

import sys

def is_valid(board, row, col):
    """Check if a queen can be placed on board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n, board, row, solutions):
    """Solve the N queens problem."""
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(n, board, row + 1, solutions)
            board[row] = -1

def print_solutions(solutions):
    """Print all solutions."""
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])

def main():
    """Main function to handle input and initiate the solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(N, board, 0, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
