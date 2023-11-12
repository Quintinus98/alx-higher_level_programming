#!/usr/bin/python3
"""Functions appends to a text file"""


def append_after(filename="", search_string="", new_string=""):
    """appends a string at the end of a text file"""
    with open(filename, "r", encoding="utf-8") as a_file:
        llist = []
        for a_line in a_file:
            llist.append(a_line)
            if search_string in a_line:
                llist.append(new_string)
    with open(filename, 'w', encoding='utf-8') as a_file:
        a_file.writelines(llist)
