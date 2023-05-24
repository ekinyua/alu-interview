#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    operations = 0
    i = 2
    while i <= n:
        while n % i == 0:
            operations += i
            n /= i
        i += 1

    if operations == 0:
        return n

    return operations
