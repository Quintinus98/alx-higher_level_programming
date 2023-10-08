#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divBy2 = []
    for elem in my_list:
        if elem % 2 == 0:
            divBy2.append(True)
        else:
            divBy2.append(False)
    return divBy2
