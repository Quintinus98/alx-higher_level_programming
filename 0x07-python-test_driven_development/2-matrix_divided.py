#!/usr/bin/python3
"""Divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Represents a matrix_divided function"""
    err = "matrix must be a matrix (list of lists) of integers/floats"
    list_len = []
    if type(matrix) is not list:
        raise TypeError(err)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(err)
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError(err)
        list_len.append(len(row))

    if len(set(list_len)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")

    new_list = [[round((e / div), 2) for e in row] for row in matrix]
    return new_list
