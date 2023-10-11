#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    flag = 0
    for k in a_dictionary.keys():
        if k == key:
            del a_dictionary[k]
            return a_dictionary
    return a_dictionary
