#!/usr/bin/python3
"""function that creates an Object from a JSON file"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    filename = "add_item.json"
    try:
        string_list = load_from_json_file(filename)
    except FileNotFoundError:
        string_list = []
    my_list = sys.argv
    for elem in my_list[1:]:
        string_list.append(elem)
    save_to_json_file(string_list, filename)


main()
