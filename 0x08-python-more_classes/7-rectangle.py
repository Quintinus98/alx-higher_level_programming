#!/usr/bin/python3
"""Defines an empty class Rectangle"""


class Rectangle:
    """Represents a class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0) -> None:
        """Initalizes a Rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of a rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns Perimeter of a rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self) -> str:
        if self.__width == 0 or self.__height == 0:
            return ("")
        string = "\n".join(str(self.print_symbol) * self.__width
                           for _ in range(self.__height))
        return string

    def __repr__(self) -> str:
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self) -> None:
        """Deleted Object"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
