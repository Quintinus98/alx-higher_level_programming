#!/usr/bin/python3
""" A function that finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """ Retrieves the peak integer in a list of integers """
    if list_of_integers is None or len(list_of_integers) == 0:
        return (None)
    peak = list_of_integers[0]
    for val in list_of_integers:
        if val > peak:
            peak = val
    return (peak)


if __name__ == '__main__':
    find_peak()
