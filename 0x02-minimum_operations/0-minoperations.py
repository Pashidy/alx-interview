#!/usr/bin/python3
"""
To calculate the min No. of Ops needed to result in exactly n H characters
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to get exactly n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations needed, or 0 if n is not achievable.
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


    return (operations)
