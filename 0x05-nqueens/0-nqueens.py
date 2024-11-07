#!/usr/bin/python3
"""Importing the sys module"""
import sys


def show_instructions_and_exit(message, exit_code=1):
    """Displays instructions and exits the program with a specified code."""
    print(message)
    sys.exit(exit_code)


def queen_is_safe(placed_queens, new_row, new_col):
    """Checks if placing a queen at (new_row, new_col) is safe from attacks."""
    for r, c in placed_queens:
        # Ensure no two queens share the same column or diagonal
        if c == new_col or abs(new_row - r) == abs(new_col - c):
            return False
    return True


def find_queen_positions(n):
    """Generates all valid solutions for placing N queens on an N x N board."""
    all_solutions = []

    def explore_board(row, queens):
        """Recursive function to place queens row by row."""
        if row == n:
            # A solution is found, save a copy of the queens list
            all_solutions.append(queens[:])
            return
        for col in range(n):
            if queen_is_safe(queens, row, col):
                queens.append([row, col])
                explore_board(row + 1, queens)
                queens.pop()  # Remove the queen to backtrack

    explore_board(0, [])
    return all_solutions


def main_program():
    """Handles input, validation, and printing of all solutions."""
    # Validate that the correct number of arguments was provided
    if len(sys.argv) != 2:
        show_instructions_and_exit("Usage: nqueens N")

    # Check that N is an integer and >= 4
    try:
        n = int(sys.argv[1])
    except ValueError:
        show_instructions_and_exit("N must be a number")
    if n < 4:
        show_instructions_and_exit("N must be at least 4")
    solutions = find_queen_positions(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main_program()
