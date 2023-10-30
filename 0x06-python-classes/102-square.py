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

    @property
    def size(self):
        """Get's the size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set's the size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __eq__(self, __value: object) -> bool:
        """Is equal"""
        return self.area() == __value.area()

    def __ne__(self, __value: object) -> bool:
        """Not equal"""
        return self.area() != __value.area()

    def __le__(self, __value: object) -> bool:
        """less than or equal"""
        return self.area() <= __value.area()

    def __lt__(self, __value: object) -> bool:
        """less than"""
        return self.area() < __value.area()

    def __ge__(self, __value: object) -> bool:
        """greater than or equal"""
        return self.area() >= __value.area()

    def __gt__(self, __value: object) -> bool:
        """greater than"""
        return self.area() > __value.area()
