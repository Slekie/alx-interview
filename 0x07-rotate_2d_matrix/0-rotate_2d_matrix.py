#!/usr/bin/python3
""" rotates 2d matrix 90 degrees """


def rotate_2d_matrix(matrix):
    """ function to rotate
    """
    # getting number of rows
    n = len(matrix)
    # traversing matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
