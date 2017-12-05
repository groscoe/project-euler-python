#!/usr/local/bin/python3
'''009_special_pythagorean_triplet.py
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''
from functools import reduce


def is_pythagoric_triplet(a: int, b: int, c: int) -> bool:
    '''Check if a, b and c form a pythagoric triplet.'''
    return a**2 + b**2 == c**2


def brute_force() -> int:
    '''Calculate the desired triplet by checking all possible combinations of
    a and b.'''
    return reduce(lambda a, b: a * b,
                  next((a, b, 1000 - (a + b))
                       for a in range(1, 1000)
                       for b in range(a, 1000)
                       if is_pythagoric_triplet(a, b, 1000 - (a + b))))


if __name__ == '__main__':
    print(brute_force())
