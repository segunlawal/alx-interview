#!/usr/bin/python3

"""
This contains an isWinner function
"""

def generate_primes(n):
    """Generates list of prime numbers between 1 and n inclusive
    """
    primes = []

    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    return primes



def isWinner(x, nums):
    """ Function determines the winner of a prime game
    Args:
        x: number of rounds
        nums: array of n
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime_numbers = generate_primes(nums[i])
        if len(prime_numbers) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
