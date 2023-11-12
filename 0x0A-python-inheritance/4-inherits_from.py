#!/usr/bin/python3
""" MyList inherits the list """


def inherits_from(obj, a_class):
    """subclass only"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
