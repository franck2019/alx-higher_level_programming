#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    res = []
    if matrix:
        for row in matrix:
            res.append(list(map(square, row)))

    return res


def square(x):
    return x**2
