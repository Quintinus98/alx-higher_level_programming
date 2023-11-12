#!/usr/bin/python3
"""function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        my_str = f.read()
        return json.loads(my_str)
