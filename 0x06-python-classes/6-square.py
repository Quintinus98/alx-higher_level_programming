#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a Square, with a size"""
    def __init__(self, size=0, position=(0, 0)) -> None:
        """Initializes the data"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Get's the size"""
        return self.__position

    @size.setter
    def position(self, pos):
        """Set's the size"""
        if not isinstance(pos, tuple) or len(pos) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(pos[0], int) or isinstance(pos[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (pos[0] < 0) or (pos[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = pos

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
