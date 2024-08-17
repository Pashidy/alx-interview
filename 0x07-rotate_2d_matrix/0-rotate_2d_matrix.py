#!/usr/bin/python3
"""Rotates a 2d matrix"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in place.

    """
    for a, b in enumerate(zip(*reversed(matrix))):
        matrix[a] = list(b)


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    """The matrix"""
    rotate_2d_matrix(matrix)
    print(matrix)
