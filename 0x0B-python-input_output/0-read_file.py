#!/usr/bin/python3
"""Functions reads a text file"""


def read_file(filename=""):
    """a function that reads a text file"""
    with open(filename, "r", encoding="utf-8") as a_file:
        print(a_file.read(), end="")
