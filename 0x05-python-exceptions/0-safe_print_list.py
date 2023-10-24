#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print("", end="\n")
    except IndexError:
        i -= 1
        print("", end="\n")
    return (i + 1)
