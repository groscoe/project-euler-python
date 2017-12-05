#!/usr/local/bin/python3
'''010_summation_of_primes.py
Find the sum of all the primes below two million.'''
from math import sqrt, ceil
from typing import List


def sieve(max_number: int) -> List[int]:
    '''Compute the sieve of Eratosthenes.'''
    primes = [False, False] + [True] * (max_number - 1)

    for number, is_prime in enumerate(primes[:ceil(sqrt(max_number)) + 1]):
        if is_prime:
            for multiple in range(number**2, max_number + 1, number):
                primes[multiple] = False

    return [number for number, is_prime in enumerate(primes) if is_prime]


def sum_of_primes_below_n(n: int) -> int:
    '''Find the sum of all primes below n using a sieve.'''
    return sum(sieve(n))


def naive_sum_of_primes_below_n(n: int) -> int:
    '''Find the sum of all primes below n using trial division.'''
    def is_prime(k: int) -> bool:
        '''Check k for primality using trial division.'''
        return not any(k % d == 0 for d in range(2, ceil(sqrt(k) + 1)))

    return 2 + sum(i for i in range(3, n, 2) if is_prime(i))


if __name__ == '__main__':
    n = 2_000_000
    print(sum_of_primes_below_n(n))
    print(naive_sum_of_primes_below_n(n))
