#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    """Represents a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = str(cls.__name__) + '.json'
        list_dict = []
        if list_objs is not None:
            for i in range(len(list_objs)):
                list_dict.append(list_objs[i].to_dictionary())
        with open(filename, 'w', encoding='utf-8') as a_file:
            return a_file.write(cls.to_json_string(list_dict))
