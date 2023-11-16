#!/usr/bin/python3
""" Module that that rotates a 2D matrix 90 degree
    clockwise
"""


def rotate_2d_matrix(matrix):
    """ edits the matrix to 90 degrees clockwise """

    # Gets the length of the matrix
    n = len(matrix)

    for a in range(n):
        # for iterating through each column
        for b in range(a):
            # for iterating through each row

            temp = matrix[a][b]
            # temp used to exchange rows to be columns and columns to be rows
            matrix[a][b] = matrix[b][a]
            matrix[b][a] = temp

    for row in matrix:
        # reverses each row in the new matrix
        row.reverse()
