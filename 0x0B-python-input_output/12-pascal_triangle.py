#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers rep the Pascal's triangle of n"""
    if n <= 0:
        return []
    pascal = [[1]]
    while len(pascal) != n:
        triangle = pascal[-1]
        temp = [1]
        for i in range(len(triangle) - 1):
            temp.append(triangle[i] + triangle[i + 1])
        temp.append(1)
        pascal.append(temp)
    return pascal
