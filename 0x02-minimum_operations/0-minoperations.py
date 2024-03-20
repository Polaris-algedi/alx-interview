#!/usr/bin/python3
"""
Greedy Algorithms: Minimum Operations to Obtain 'H' Characters
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to
    obtain n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required.
        If n is less than or equal to 1, returns 0.

    Notes:
        In order to solve this problem efficiently, you should understand
        the following concepts:
        1. Prime factorization: Breaking down a number into its prime factors.
        Adding the prime factors of a number will magically be the number of
        operations needed to obtain that number of 'H' characters.
        2. "If b is a multiple of a, then any number divisible by b is also
        divisible by a.": Knowing this rule simplifies the solution process
        because only prime factors will be added as operations, and non-prime
        numbers will not contribute to the operation count.

    Example:
        >>> minOperations(9)
        6
        >>> minOperations(4)
        4
        >>> minOperations(12)
        7
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
