#!/usr/bin/python3


def sieve_of_Eratosthenes(n):
    '''
    return a list of prime number less or equal n
    using : Sieve of Eratosthenes Algorithm
    '''

    primes = [True for i in range(n + 1)]
    primes[0] = primes[1] = False
    p = 2

    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False

        p += 1

    return [i for i, is_prime in enumerate(primes) if is_prime]


def calculate_moves(n):
    """
    Calculate the number of moves possible for a given n
    """
    primes = sieve_of_Eratosthenes(n)
    count = 0
    visited = [False] * (n + 1)

    for prime in primes:
        if not visited[prime]:
            count += 1
            for multiple in range(prime, n + 1, prime):
                visited[multiple] = True

    return count


def isWinner(x, nums):
    """ who is the winner, Maria or Ben """

    if x < 1 or not nums:
        return None

    marias_wins = 0
    bens_wins = 0

    for n in nums:
        moves = calculate_moves(n)

        if moves % 2 == 0:
            bens_wins += 1
        else:
            marias_wins += 1

    if marias_wins > bens_wins:
        return "Maria"
    elif bens_wins > marias_wins:
        return 'Ben'
    else:
        return None
