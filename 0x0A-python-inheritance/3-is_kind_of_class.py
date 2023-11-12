#!/usr/bin/python3
""" MyList inherits the list """


def is_kind_of_class(obj, a_class):
    """Same class or inherit"""
    return True if isinstance(obj, a_class) else False
