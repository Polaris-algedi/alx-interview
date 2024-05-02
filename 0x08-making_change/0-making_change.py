#!/usr/bin/python3
"""
makeChange takes a list of coins and a total amount, and returns
the minimum number of coins needed to make that total.
"""


def makeChange(coins, total):
    """Function makeChange takes a list of coins and a total amount,
    and returns the minimum number of coins needed to make that total.

    Args:
        coins (list): A list of integers representing the values of coins.
        total (int): An integer representing the total amount to be made.

    Returns:
        int: An integer representing the minimum number of coins needed to
        make the total, or -1 if the total cannot be made.

    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins needed for
    # each total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp array for each possible total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still float('inf'), it means total cannot be met
    # by any combination of coins
    return dp[total] if dp[total] != float('inf') else -1
