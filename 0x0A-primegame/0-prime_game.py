#!/usr/bin/python3
"""Prime Game execution"""


def sieve_of_eratosthenes(max_n):
    """Generate a list indicating prime status up to max_n using Sieve of Eratosthenes."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    return is_prime


def count_primes_up_to_n(is_prime, n):
    """Count how many primes exist from 1 to n using the is_prime list."""
    count = 0
    for i in range(1, n + 1):
        if is_prime[i]:
            count += 1
    return count


def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_up_to_n(is_prime, n)
        # If the number of primes is odd, Maria wins; if even, Ben wins.
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
