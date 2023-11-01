#!/usr/bin/python3
"""
This module provides solution for an interview question
`The N queens puzzle` in which there is a challenge of
placing N non-attacking queens on an N x N chessboard
"""
import sys


def nqueens(n):
    """ A function that provides the solution to the challenge """
    if type(n) is not int:
        # if the input is not a number
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        # if the input is lesser than 4
        print("N must be at least 4")
        sys.exit(1)

    # A list to keep track of the good positions
    result = []

    def backtrack(queen, row_and_col, row_minus_col):
        """ a helper function for the nqueens """
        row = len(queen)
        if row == n:
            result.append(queen.copy())
            return

        for col in range(n):
            if col not in queen and row + col not in row_and_col\
               and row - col not in row_minus_col:
                backtrack(queen + [col], row_and_col + [row + col],
                          row_minus_col + [row - col])

    backtrack([], [], [])

    for queens in result:
        print([[a, queens[a]]for a in range(n)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(n)
