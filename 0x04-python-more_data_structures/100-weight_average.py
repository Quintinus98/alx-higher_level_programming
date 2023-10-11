#!/usr/bin/python3
def weight_average(my_list=[]):
    if not bool(my_list):
        return 0
    divisor = 0
    numerator = 0
    for elem in my_list:
        divisor += elem[1]
        mul = elem[0] * elem[1]
        numerator += mul
    return (numerator/divisor)
