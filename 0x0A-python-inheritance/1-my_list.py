#!/usr/bin/python3
""" MyList inherits from list """


class MyList(list):
    """ Represents a class that inherits from list """
    def __init__(self):
        """Initializes the super class"""
        super().__init__()

    def print_sorted(self):
        """ Prints a sorted list """
        print(sorted(self))
