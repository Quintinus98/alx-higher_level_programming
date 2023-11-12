#!/usr/bin/python3
"""Functions writes to a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as a_file:
        a_file.write(text)
