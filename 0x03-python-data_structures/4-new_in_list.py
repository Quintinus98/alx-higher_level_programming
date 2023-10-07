#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_cpy = my_list[:]
    if idx >= len(list_cpy) or idx < 0:
        return list_cpy
    list_cpy[idx] = element
    return list_cpy
