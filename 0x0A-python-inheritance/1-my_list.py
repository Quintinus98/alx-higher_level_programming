#!/usr/bin/python3
""" MyList inherits the list """


class MyList(list):
    """ Represents a subclass of list """

    def print_sorted(self):
        """ Prints a sorted list """
        print(sorted(self))
