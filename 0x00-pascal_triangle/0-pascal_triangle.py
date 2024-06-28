#!/usr/bin/python3
"""
Return a list of integers representing Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(factorial(i) // (factorial(j) * factorial(i - j)))
        triangle.append(row)

    return triangle


def factorial(n):
    """
    Return the factorial of n.
    """
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f
