#!/usr/bin/python3
""" This module provides a function that determines
    the fewest number of coins needs to meet a given
    amount.
"""


def makeChange(coins, total):
    """ returns the fewest number of coins needed """
    if total <= 0:
        return 0

    # Sort coins in descending order
    sorted_coins = sorted(coins, reverse=True)

    used_coins = 0  # Counts the number of coins used
    balance = total  # Tracks the balance to make up

    # go through the available coins denomination
    for coin in sorted_coins:
        # check if current coin is not greater than the remaining total
        while balance % coin >= 0 and balance >= coin:
            # Increment the used coins and update the balance
            used_coins += int(balance / coin)
            balance = balance % coin

    # Checks if the coins could successfully meet the total
    if balance != 0:
        used_coins = -1

    return used_coins
