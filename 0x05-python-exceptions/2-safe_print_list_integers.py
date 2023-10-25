#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        n = 0
        for i in range(x):
            if not isinstance(my_list[i], int):
                continue
            print("{:d}".format(my_list[i]), end="")
            n += 1
        print("", end="\n")
    except IndexError as err:
        raise
    return n
