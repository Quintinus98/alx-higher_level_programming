#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for em in my_list:
        if em == search:
            em = replace
        new_list.append(em)
    return new_list
