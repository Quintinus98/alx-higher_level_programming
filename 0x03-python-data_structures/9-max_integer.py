#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    for em in my_list:
        if em > max:
            max = em
    return max
