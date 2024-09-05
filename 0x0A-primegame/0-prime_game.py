#!/usr/bin/python3
"""Prime Game execution"""


def prime_numbers(n):
    """Returns a list of prime numbers between 1 and n inclusive.

    Args:
        n (int): The upper boundary. The lower boundary is always 1.

    Returns:
        list: A list of prime numbers up to and including n.
    """
    if n < 2:
        return [0] * (n + 1)

    primes = [1] * (n + 1)
    primes[0], primes[1] = 0, 0  # 0 and 1 are not primes

    for i in range(2, int(n**0.5) + 1):
        if primes[i] == 1:
            for j in range(i * i, n + 1, i):
                primes[j] = 0  # Mark multiples of i as not prime

    return primes


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): The number of rounds of the game.
        nums (list of int): The upper limit of the range for each round.

    Returns:
        str: The name of the winner, or None if no clear winner.
    """
    if x <= 0 or not nums:
        return None

    # Initialize counts for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Find the maximum number to generate primes up to that number
    max_num = max(nums)
    primes = prime_numbers(max_num)

    # Determine the winner per round
    for n in nums:
        prime_count = sum(primes[:n + 1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
