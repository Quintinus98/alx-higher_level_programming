#!/usr/bin/python3
""" MyList inherits the list """


def inherits_from(obj, a_class):
    """Same class or sub"""
    return True if issubclass(obj, a_class) else False
