#!/usr/bin/python3
"""An empty class BaseGeometry."""


class BaseGeometry:
    """Represents a BaseGeometry Class"""
    def area(self):
        """defines area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integer for type and value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
