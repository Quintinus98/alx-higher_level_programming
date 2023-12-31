#!/usr/bin/python3
"""Prints a square"""


def print_square(size):
    """Prints a square with character #"""
    if (type(size) is not int or (type(size) is float and size < 0)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
