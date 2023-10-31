#!/usr/bin/python3
""" Addition function """


def add_integer(a, b=98):
    """Adds two integers"""
    if (type(a) is not int and type(a) is not float):
        return TypeError("a must be an integer")
    if (type(b) is not int and type(b) is not float):
        return TypeError("b must be an integer")
    return (int(a) + int(b))
