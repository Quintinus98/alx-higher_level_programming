#!/usr/bin/python3
def max_integer(my_list=[]):
    if not bool(my_list):
        return None
    maxi = my_list[0]
    for em in my_list:
        if em > maxi:
            maxi = em
    return maxi
