#!/usr/bin/python3
"""Pascal's triangle module."""


def pascal_triangle(n):
    """Function to return Pascal's triangle of size n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    pascal = []
    for i in range(n):
        row = [1]

        if i > 0:
            for j in range(1, i):
                row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
            row.append(1)
        pascal.append(row)
    return pascal
