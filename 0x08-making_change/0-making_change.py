#!/usr/bin/python3
'''Making changes problem'''


def get_coins_count(start, coins, total):
    ''' get the number of coins needed to get a total coins needed'''
    if total < start:
        return -1

    origin_total = total
    total -= start
    count_coins = 1  # I will use it to count how many coins i used
    sum_coins = start
    for x in coins:

        while total - x >= 0 and total >= 0:
            total -= x
            count_coins += 1
            sum_coins += x

    if total != 0 or sum_coins != origin_total:
        return -1

    return count_coins


def makeChange(coins, total):
    ''' solving the making change problem'''
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    list_of_counts = []

    i = 0
    for start in coins:

        coins_count = get_coins_count(start, coins[i:], total)
        list_of_counts.append(coins_count)
        i += 1

    if max(list_of_counts) == -1:
        return -1

    # removing all -1 if there are any
    list_of_counts = [c for c in list_of_counts if c != -1]

    list_of_counts.sort()

    return list_of_counts[0]
