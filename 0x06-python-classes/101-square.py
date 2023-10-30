#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a Square, with a size"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data
        Args:
            size (int): Integer
            position (int, int): Tuple
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get's the size"""
        return (self.__size)

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
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set's the position"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or isinstance(value[1], int) or
                not value[0] >= 0 or not value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints # and spaces"""
        if self.__size == 0:
            print("")
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")

    def __str__(self):
        """Prints a square"""
        if self.__size != 0:
            [print("") for _ in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            [print("#", end="") for _ in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
