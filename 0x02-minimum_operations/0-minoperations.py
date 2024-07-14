#!/usr/bin/python3
"""
To calculate the min No. of Ops needed to result in exactly n H characters
"""


def minOperations(n):
    """
    Min Ops
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

