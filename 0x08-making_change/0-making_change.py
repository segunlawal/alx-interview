#!/usr/bin/python3

"""
This contains a makeChange function
"""


def makeChange(coins, total):
    """ Function determines the fewest number of coins needed to meet a given amount total"""
    if total <= 0:
        return 0
    
    minCoins = [0] + [total + 1] * total

    for amount in range(1, total + 1):
        # Try each coin denomination to find the minimum number of coins needed
        for coin in coins:
            if amount - coin >= 0:
                minCoins[amount] = min(minCoins[amount], minCoins[amount - coin] + 1)

    if minCoins[total] < total + 1:
        return minCoins[total]

    # If the final entry is still greater than the total, return
    return -1
