#!/usr/bin/python3
"""
A function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after
    each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    next = 0
    for ch in text:
        if next == 0:
            if ch == ' ':
                continue
            next = 1
        if next == 1:
            if ch == '.' or ch == '?' or ch == ":":
                print(ch, end="\n")
                print()
                next = 0
            else:
                print(ch, end="")
