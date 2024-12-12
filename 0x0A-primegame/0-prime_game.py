#!/usr/bin/python3
"""Prime game module.
"""

def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds
    """
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def play_round(n):
        primes = [num for num in range(2, n + 1) if is_prime(num)]
        player = 0  # 0 for Maria, 1 for Ben
        while primes:
            if not primes:
                break
            p = primes.pop(0)
            for i in range(len(primes) - 1, -1, -1):
                if primes[i] % p == 0:
                    primes.pop(i)
            player ^= 1
        return player

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_round(n)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
