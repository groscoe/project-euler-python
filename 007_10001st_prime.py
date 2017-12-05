#!/usr/local/bin/python3
'''007_10001st_prime.py
Calculate the 10 001st prime number'''
from math import sqrt


def naive_nth_prime(n: int) -> int:
    '''Calculate the nth prime by trial division.'''
    if n == 1:
        return 2

    def is_prime(n: int) -> bool:
        '''Check n for primality.'''
        return all(n % k != 0 for k in range(2, int(sqrt(n)) + 1))

    counter = 2
    number = 3
    while counter < n:
        number += 2  # ignore even numbers
        if is_prime(number):
            counter += 1

    return number


if __name__ == '__main__':
    n = 10_001
    print(naive_nth_prime(n))
