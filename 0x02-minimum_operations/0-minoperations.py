#!/usr/bin/python3
"""
This module defines a fxn to calculate the min no. of Ops
needed to get exactly n 'H' Xters in a text file starting with a single 'H'.
"""


def minOperations(n):
    """
    Calculate the min no. of operations needed to get exactly n 'H' characters

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum no. of operations needed, or 0 if n isnt achievable.
    """
    if n <= 1:
        return 0


    operations = 0
    factor = 2


    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1


    return operations
