#!/usr/bin/python3
"""
To determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sort coins in descending order to ensure larger denominations first
    coins.sort(reverse=True)

    # Create a dp array with 'infinity' to represent unreachable amounts
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to reach a total of 0
    dp[0] = 0

    # Loop through each coin and update dp for possible totals
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
