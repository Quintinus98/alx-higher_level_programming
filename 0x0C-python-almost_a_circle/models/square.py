#!/usr/bin/python3
"""Class Square inherits from class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the Square class"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """String representation"""
        str1 = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        str2 = "{}/{} - {}".format(self.x, self.y, self.size)
        return (str1 + str2)

    @property
    def size(self):
        return self.__size
