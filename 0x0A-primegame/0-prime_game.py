#!/usr/bin/python3
"""Prime Game execution"""


def sieve_of_eratosthenes(max_n):
    """
    Generate a list of primes up to max_n using the Sieve of Eratosthenes.
    """
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    return [i for i in range(max_n + 1) if is_prime[i]]


def count_primes(n, primes):
<<<<<<< HEAD
    """Count how many primes exist from 1 to n using the primes list."""
=======
    """
    Count how many primes exist from 1 to n using the primes list.
    """
>>>>>>> ae7692d06a0b1277fc9f19f3a1557cf67e114346
    count = 0
    for prime in primes:
        if prime > n:
            break
        count += 1
    return count


def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    # Determine the maximum number in nums to generate primes up to that number
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes(n, primes)
        # If the count of primes is odd, Maria wins, otherwise Ben wins
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
