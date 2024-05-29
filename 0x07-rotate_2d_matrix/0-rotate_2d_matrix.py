#!/usr/bin/python3
""" Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """ Rotate a 2D matrix 90 degrees clockwise"""
    n = len(matrix)
    m = len(matrix) - 1
    matrix1 = [r[:] for r in matrix]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = matrix1[m - j][i]
