#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    flag = 0
    for k in a_dictionary.keys():
        if k == key:
            a_dictionary[k] = value
            flag = 1
    if not flag:
        a_dictionary[key] = value
    return a_dictionary
