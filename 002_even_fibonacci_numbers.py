#!/usr/local/bin/python3
'''002_even_fibonacci_numbers.py
By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.'''
from typing import Generator
from itertools import takewhile


def fib_numbers() -> Generator[int, None, None]:
    '''Calculate and yield each term in the Fibonacci sequence.'''
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


def fib_numbers_below_k(k: int) -> Generator[int, None, None]:
    '''Yield all terms in the Fibonacci sequence smaller than k.'''
    yield from takewhile(lambda x: x < k, fib_numbers())


def sum_even_fib_numbers_below_k(k: int) -> int:
    '''Sum all even terms in the Fibonacci sequence smaller than k.'''

    return sum(filter(lambda x: x % 2 == 0, fib_numbers_below_k(k)))


if __name__ == '__main__':
    k = 4_000_000
    print(sum_even_fib_numbers_below_k(k))
