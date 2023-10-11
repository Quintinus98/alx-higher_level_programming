#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not bool(roman_string):
        return 0
    sum = 0
    rd = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(roman_string) == 1:
        return rd[roman_string]
    for i in range(0, len(roman_string) - 1):
        if rd[roman_string[i]] >= rd[roman_string[i + 1]]:
            sum += rd[roman_string[i]]
        else:
            sum -= rd[roman_string[i]]
        if i == len(roman_string) - 2:
            sum += rd[roman_string[i + 1]]
    return sum
