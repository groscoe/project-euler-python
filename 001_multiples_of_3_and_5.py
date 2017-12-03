#!/usr/local/bin/python3
'''001_multiples_of_3_and_5.py
Project Euler - Problem 1

Find the sum of all the multiples of 3 or 5 below 1000.'''
from math import gcd

def brute_force(m: int, n: int, k: int) -> int:
    '''Solve by summing every number below k except the multiples
    of m and n'''
    return sum(i for i in range(k) if i % m == 0 or i % n == 0)


def solve_intelligently(m: int, n: int, k: int) -> int:
    '''Subtract the sum of multiples of both m and n below k from the sum
    of multiples of m or n below k'''
    def sum_of_1_to_n(n: int) -> int:
        '''Sum all integers from 1 to n.'''
        return n * (n + 1) // 2

    def sum_of_multiples_of_n_below_k(n: int, k: int) -> int:
        '''Sum all multiples of n smaller than k'''
        number_of_multiples: int = (k - 1) // n
        return n * sum_of_1_to_n(number_of_multiples)

    def lcm(x: int, y: int) -> int:
        '''Find the least common multiple of x and y by reducing the problem
        to finding their greatest common divisor'''
        return (x * y) // gcd(x, y)

    return (sum_of_multiples_of_n_below_k(m, k) +
            sum_of_multiples_of_n_below_k(n, k) -
            sum_of_multiples_of_n_below_k(lcm(m, n), k))


if __name__ == '__main__':
    m, n, k = 3, 5, 1000
    print(f'Result by deduction: {solve_intelligently(m, n, k)}')
    print(f'Result by brute force: {brute_force(m, n, k)}')
