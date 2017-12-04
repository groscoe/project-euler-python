#!/usr/local/bin/python3
'''006_sum_square_difference.py
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.'''
from typing import Generator


def squares(n: int) -> Generator[int, None, None]:
    '''Yield the square of the n first natural numbers.'''
    yield from map(lambda x: x * x, range(1, n + 1))


def brute_force(n: int) -> int:
    '''Solve by computing the difference explicitly.'''
    sum_of_squares = sum(squares(n))
    square_of_the_sum = sum(range(1, n + 1))**2
    return square_of_the_sum - sum_of_squares


def sum_of_squares_from_1_to_n(n: int) -> int:
    '''Compute the sum of i**2 from i=1 to n using the solution of the
    summation.'''
    return n * (n + 1) * (2 * n + 1) // 6


def sum_from_1_to_n(n: int) -> int:
    '''Compute the sum of the first n integers.'''
    return n * (n + 1) // 2


def solve_using_the_formulas(n: int) -> int:
    '''Solve the problem using the formulas obtained by solving the
    summations.'''
    return (sum_from_1_to_n(n)**2 - 
            sum_of_squares_from_1_to_n(n))


if __name__ == '__main__':
    n = 100
    print(solve_using_the_formulas(n))
    print(brute_force(n))
