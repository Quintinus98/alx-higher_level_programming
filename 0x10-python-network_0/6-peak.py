#!/usr/bin/python3
""" A function that finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """ Retrieves the peak integer in a list of integers """
    if list_of_integers is None or len(list_of_integers) == 0:
        return (None)

    arr = list_of_integers  # name is too long.
    n = len(arr)
    start = 0
    end = n - 1

    if start == end:
        return arr[0]
    mid = (start + end) // 2

    # if just 2 elems are remaining, return the greater one.
    if mid == 0:
        return arr[mid] if arr[mid] > arr[end] else arr[end]

    if arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
        return arr[mid]

    # Peak is in left half
    if arr[mid - 1] > arr[mid]:
        return find_peak(arr[:mid])
    else:
        return find_peak(arr[mid:])


if __name__ == '__main__':
    find_peak()
