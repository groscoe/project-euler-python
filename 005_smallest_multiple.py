#!/usr/local/bin/python3
'''005_smallest_multiple.py
Calculate the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20.'''
from math import gcd
from typing import Sequence
from functools import reduce


def lcm(a: int, b: int) -> int:
    '''Calculate the least common multiple of a and b.'''
    return a * b // gcd(a, b)


def lcm_of_sequence(l: Sequence[int]) -> int:
    '''Calculate the lcm of a sequence of numbers.'''
    return reduce(lcm, l)


def lcm_of_all_from_1_to_n(n: int) -> int:
    '''Find the lcm of all numbers from 1 to n.'''
    return lcm_of_sequence(range(2, n))


if __name__ == '__main__':
    n = 20
    print(lcm_of_all_from_1_to_n(n))
