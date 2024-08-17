#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list[list[int]]): A 2D matrix to rotate.
    """
    n = len(matrix)

    # Transpose the matrixfor i inrange(n):
    for j inrange(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each rowfor i inrange(n):
        matrix[i].reverse()


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
