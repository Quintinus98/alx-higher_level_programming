#!/usr/bin/python3
"""Functions appends to a text file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, "a", encoding="utf-8") as a_file:
        a_file.write(text)
