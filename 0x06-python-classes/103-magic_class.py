#!/usr/bin/python3
"""Define a Magic class from bytecode"""

import math


class MagicClass:
    """Represents a circle class"""

    def __init__(self, radius=0):
        """Initializes the MagicClass
        Args:
            radius (int or float): Radius of circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of a circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns the circumference of a circle"""
        return (2 * math.pi * self.__radius)
