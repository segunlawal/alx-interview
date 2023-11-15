#!/usr/bin/python3

"""
This contains a 2D matrix rotation function
"""


def rotate_2d_matrix(matrix):
    """ Function rotates a 2D matrix 90 degrees clockwise"""

    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
