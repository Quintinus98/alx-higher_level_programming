#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a Square, with a size"""
    def __init__(self, size=0) -> None:
        """Initializes the data"""
        self.__size = size
