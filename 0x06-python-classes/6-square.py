#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a Square, with a size"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get's the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set's the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get's the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set's the position"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints # and spaces"""
        if self.__size == 0:
            print("")
        else:
            [print("") for _ in range(self.__position[1])]
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
