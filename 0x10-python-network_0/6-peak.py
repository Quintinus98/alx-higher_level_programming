#!/usr/bin/python3
""" A function that finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """ Retrieves the peak integer in a list of integers """
    if list_of_integers is None or len(list_of_integers) == 0:
        return (None)
    arr = list_of_integers
    n = len(arr)
    if n == 1:
        return arr[0]
    for i in range(n):
        # first element is greater than its only neighbour
        if i == 0 and arr[i] >= arr[i + 1]:
            return arr[i]
        # last element is greater than its only neighbour
        if i == n - 1 and arr[i] >= arr[i - 1]:
            return arr[i]
        # It is greater than its left and right neighbours
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return arr[i]


if __name__ == '__main__':
    find_peak()
