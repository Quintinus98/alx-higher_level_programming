#!/usr/bin/python3
""" MyList inherits the list """


class MyList(list):
    """ Represents a subclass of list """
    def __init__(self):
        """Initializes the base class"""
        super().__init__()

    def print_sorted(self):
        """ Prints a sorted list """
        print(sorted(self))
