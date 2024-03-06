#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n

    Args:
        n: The number of rows to generate. Must be a non-negative integer.

    Returns:
        A list of lists representing the first n rows of Pascal's triangle.
        Returns an empty list if n is less than or equal to 0,
        as Pascal's triangle is not defined for non-positive values of n.
    """

    if n > 1:
        triangle = pascal_triangle(n - 1)
        row = triangle[n - 2]
        new_row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)]
        new_row += [1]
        triangle.append(new_row)
        return triangle
    elif n == 1:
        """
        Returns the first row of Pascal's triangle, which is simply [1].
        """
        return [[1]]
    else:
        """
        Returns an empty list if n is less than or equal to 0.
        """
        return []
