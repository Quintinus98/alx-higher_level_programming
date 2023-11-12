#!/usr/bin/python3
"""function that returns the dictionary description with data structure"""


def class_to_json(obj):
    """returns the dictionary description with data structure"""
    return obj.__dict__
