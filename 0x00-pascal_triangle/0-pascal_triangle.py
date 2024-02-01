#!/usr/bin/python3

"""
This contains a pascal triangle function
"""


def pascal_triangle(n):
    """ Function returns a list of lists of integers
     representing the Pascal’s triangle of n """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        row = [1]
        prev_row = triangle[-1]
        for i in range(len(prev_row) - 1):
            row.append(prev_row[i] + prev_row[i + 1])
        row.append(1)
        triangle.append(row)

    return triangle
