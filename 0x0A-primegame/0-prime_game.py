#!/usr/bin/python3
""" This module provides solution to
    the prime game
"""


def rm_multiples(lists, x):
    """ removes multiples of a prime number """
    for a in range(2, len(lists)):
        try:
            lists[a * x] = 0
        except (ValueError, IndexError):
            break


def isWinner(x, nums):
    """ checks and returns the winner """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    maria_wins = 0
    ben_wins = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for n in range(2, len(a)):
        rm_multiples(a, n)

    for n in nums:
        if sum(a[0:n + 1]) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif maria_wins < ben_wins:
        return 'Ben'
    else:
        return None
