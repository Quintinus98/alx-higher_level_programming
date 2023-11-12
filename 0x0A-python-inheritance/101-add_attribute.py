#!/usr/bin/python3
"""Adds a new attribute to an object if it's possible"""


def add_attribute(theObject, param, value):
    """Adds a new attribute"""
    if not hasattr(theObject, "__dict__"):
        raise TypeError("can't add new attribute")
    return setattr(theObject, param, value)
