#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for row in matrix:
        squared.append([(em ** 2) for em in row])
    return squared
