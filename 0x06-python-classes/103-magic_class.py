#!/usr/bin/python3
"""Magic class from bytecode"""

import math


class MagicClass:
    """Represents a magic class"""
    def __init__(self, radius=0):
        """Initializes the radius"""
        self._MagicClass__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Computes the area"""
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """Circumference of a circle"""
        return (2 * math.pi * self._MagicClass__radius)
