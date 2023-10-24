#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = -1
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print("", end="\n")
    except IndexError:
        i -= 1
        print("", end="\n")
    return (i + 1)


my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 5)
print("nb_print: {:d}".format(nb_print))
