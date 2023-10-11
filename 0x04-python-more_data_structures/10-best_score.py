#!/usr/bin/python3
def best_score(a_dictionary):
    if not bool(a_dictionary):
        return (None)
    max = -1000
    string = ""
    for k in a_dictionary.keys():
        if a_dictionary[k] > max:
            max = a_dictionary[k]
            string = k
    return string
