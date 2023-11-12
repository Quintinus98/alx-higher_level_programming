#!/usr/bin/python3
"""A sub class Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a Rectangle Class"""
    def __init__(self, width, height):
        """Initializes the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Str documentation"""
        return ("[{}] {}/{}".format(type(self).__name__,
                self.__width, self.__height))
