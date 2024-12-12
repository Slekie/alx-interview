#!/usr/bin/python3
""" determining fewest number of coins needed to meet given amount """


def makeChange(coins, total):
    if total <= 0:
        return 0

    count = 0
    coins.sort(reverse=True)
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1

            if total == 0:
                break
    if total != 0:
        return -1

    return count
