#!/usr/bin/python3
"""A sub class Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Rectangle Class"""
    def __init__(self, size):
        """Initializes the Square"""
        self.integer_validator("size", size)
        self.__size = size
