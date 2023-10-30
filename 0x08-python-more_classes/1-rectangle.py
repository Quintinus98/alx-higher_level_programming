#!/usr/bin/python3
"""Defines an empty class Rectangle"""


class Rectangle:
    """Represents a class Rectangle"""

    def __init__(self, width=0, height=0) -> None:
        """Initalizes a Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves or Sets the Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves or Sets the Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
