#!/usr/bin/python3
"""
Nothing imported
"""


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_count(n):
    """Count prime numbers from 1 to n inclusive."""
    primes = [True] * (n + 1)  # Sieve of Eratosthenes approach
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    count = 0
    for i in range(2, n + 1):
        if primes[i]:  # If i is prime
            count += 1
            for j in range(i * 2, n + 1, i):
                primes[j] = False
    return count


def isWinner(x, nums):
    """
    Determines the winner of x rounds of the prime game.

    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben").
    """
    if x < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    max_n = max(nums)
    prime_counts = [0] * (max_n + 1)

    # Precompute number of primes from 1 to max_n
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if is_prime(i) else 0)

    for n in nums:
        if prime_counts[n] % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
