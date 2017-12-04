#!/usr/local/bin/python3
'''004_largest_palindrome_product.py
Find the largest palindrome made from the product of two 3-digit numbers.'''
from typing import Generator


def reversed_products_of_n_digits(n: int) -> Generator[int, None, None]:
    '''Yield each product of two n-digit numbers.'''
    largest_number = 10**n - 1
    smallest_number = 10**(n - 1)

    for i in range(largest_number, smallest_number - 1, -1):
        for j in range(i, smallest_number - 1, -1):
            yield i * j
    return None


def is_palindromic(n: int) -> bool:
    '''Check if a number is palindromic by reversing its string
    representation.'''
    representation = str(n)

    return representation == representation[::-1]


def brute_force_solve(n: int) -> int:
    '''Find the largest palindromic product of two n-digit integers by
    iterating until the largest palindromic product is found'''
    return max(filter(is_palindromic, reversed_products_of_n_digits(n)))


def better_brute_force_solve(n: int) -> int:
    '''Alternative brute force solution that avoids calculating every
    possible product by stopping when the products get too small.'''
    largest_number = 10**n - 1
    smallest_number = 10**(n - 1)
    largest_palindrome_found = 0

    for i in range(largest_number, smallest_number - 1, -1):
        for j in range(i, smallest_number - 1, -1):
            product = i * j
            if product <= largest_palindrome_found:
                break
            if is_palindromic(product):
                largest_palindrome_found = product

    return largest_palindrome_found


if __name__ == '__main__':
    num_digits = 3
    print(better_brute_force_solve(num_digits))
    print(brute_force_solve(num_digits))
