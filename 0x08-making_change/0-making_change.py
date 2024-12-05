#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a given amount.
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins required to meet the given total.

    Args:
        coins (list): A list of the values of coins available.
        total (int): The total amount to make change for.

    Returns:
        int: The fewest number of coins needed, or -1 if change cannot be made.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    count = 0  # To keep track of the number of coins used
    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin

    return count if total == 0 else -1
