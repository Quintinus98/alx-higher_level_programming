#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not bool(roman_string):
        return 0
