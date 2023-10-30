#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a Square, with a size"""
    def __init__(self, size=0) -> None:
        """Initializes the data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
