#!/usr/bin/python3
import math
"""Magic class from bytecode"""


class MagicClass:
    """Represents a magic class"""
    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Computes the area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Circumference of a circle"""
        return (2 * math.pi * self.__radius)