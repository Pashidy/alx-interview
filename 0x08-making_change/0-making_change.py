#!/usr/bin/python3
"""
To determine the fewest number of coins needed to meet a given amount total.
"""
from collections import deque


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize a queue for BFS
    queue = deque([(0, 0)])  # (Current total, number of coins)
    visited = set([0])

    while queue:
        current_total, num_coins = queue.popleft()

        for coin in coins:
            next_total = current_total + coin
            if next_total == total:
                return num_coins + 1
            if next_total > total:
                continue
            if next_total not in visited:
                visited.add(next_total)
                queue.append(
                        (next_total, num_coins + 1)
                )

    return -1
