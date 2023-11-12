#!/usr/bin/python3
"""Class MyInt inherits int"""


class MyInt(int):
    """Represents a rebel subclass of int"""
    def __eq__(self, other):
        """equal is now not equal"""
        return int(self) != other

    def __ne__(self, other):
        """not equal is now equal"""
        return int(self) == other
