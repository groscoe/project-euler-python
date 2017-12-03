#!/usr/local/bin/python3
'''003_largest_prime_factor.py
Calculate the largest prime factor of the number 600851475143'''
from math import sqrt, gcd
from typing import List, Callable
from functools import lru_cache


@lru_cache()  # memoization
def naive_factorize(n: int) -> List[int]:
    '''Decompose n in its prime factors, if any, recursively.'''

    def divides(k, m):
        '''Verify if k divides m evenly.'''
        return m % k == 0

    if n <= 1:
        return []
    if divides(2, n):  # small optimization, remove factors of two quickly.
        return [2] + naive_factorize(n // 2)
    for potential_divider in range(3, int(sqrt(n)), 2):
        if divides(potential_divider, n):
            return ([potential_divider] +
                    naive_factorize(n // potential_divider))
    return [n]


def pollard_rho_factorize(n: int) -> List[int]:
    '''Factorize an integer using the Pollard's rho algorithm.
    Adapted from https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
    It doesn't really make a difference in this case, but is much faster with
    larger inputs.'''
    def g(x: int) -> int:
        '''A polynomial in x computed modulo n.'''
        return (x**2 + 1) % n

    x, y, factor = 2, 2, 1

    while factor == 1:
        x = g(x)
        y = g(g(y))
        factor = gcd(abs(x - y), n)

    if factor == n:
        return [n]

    return [factor] + pollard_rho_factorize(n // factor)


def greatest_prime_factor(n: int,
                          factorizer: Callable[[int], List[int]]) -> int:
    '''Find the greatest prime factor of n by navie factorization.'''
    return max(factorizer(n))


if __name__ == "__main__":
    n = 600851475143
    print(greatest_prime_factor(n, naive_factorize))
    print(greatest_prime_factor(n, pollard_rho_factorize))
