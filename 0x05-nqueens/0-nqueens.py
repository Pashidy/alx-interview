#!/usr/bin/python3
"""
This script solves the N queens puzzle.
"""

import sys


def solve_queens_problem(board_size):
    """
    Solve the N queens problem.

    Args:
        board_size (int): The size of the chessboard (N).

    Returns:
        list: A list of solutions, each solution is a list
    """
    def is_valid_position(pos, occupied_pos):
        """
        Check if a position is valid for placing a queen.

        Args:
            pos (int): The current column position for the queen.
            occupied_pos (list): List of occupied positions by queens.

        Returns:
            bool: True if the position is valid, False otherwise.
        """
        for i in range(len(occupied_pos)):
            if (
                occupied_pos[i] == pos or
                occupied_pos[i] - i == pos - len(occupied_pos) or
                occupied_pos[i] + i == pos + len(occupied_pos)
            ):
                return False
        return True

    def place_queens(board_size, index, occupied_pos, solutions):
        """
        Recursively place queens on the board.

        Args:
            board_size (int): The size of the chessboard (N).
            index (int): The current row index.
            occupied_pos (list): List of occupied positions by queens.
            solutions (list): List to store the valid solutions.
        """
        if index == board_size:
            solutions.append(occupied_pos[:])
            return

        for i in range(board_size):
            if is_valid_position(i, occupied_pos):
                occupied_pos.append(i)
                place_queens(board_size, index + 1, occupied_pos, solutions)
                occupied_pos.pop()

    solutions = []
    place_queens(board_size, 0, [], solutions)
    return solutions


def main():
    """
    Main function to handle input and initiate the solver.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_queens_problem(board_size)
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == "__main__":
    main()
