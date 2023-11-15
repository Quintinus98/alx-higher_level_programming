#!/usr/bin/python3
"""Base Class"""
import json
import os
import csv


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
        return json.dumps(list_dictionaries, indent=2)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        filename = str(cls.__name__) + '.json'
        list_dict = []
        if list_objs is not None:
            for i in range(len(list_objs)):
                list_dict.append(list_objs[i].to_dictionary())
        with open(filename, 'w', encoding='utf-8') as a_file:
            return a_file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        else:
            raise NameError('Cannot match class name')
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = str(cls.__name__) + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, mode="r", encoding="utf-8") as a_file:
            my_cls = cls.from_json_string(a_file.read())
            return [cls.create(**l_dict) for l_dict in my_cls]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ writes the JSON string representation of list_objs to csv file"""
        filename = str(cls.__name__) + '.csv'
        clsList = []
        if list_objs is not None:
            clsList = [list(obj.to_dictionary().values()) for obj in list_objs]
        with open(filename, 'w', encoding='utf-8') as a_file:
            csv_writer = csv.writer(a_file)
            for row in clsList:
                csv_writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of instances"""
        filename = str(cls.__name__) + ".csv"
        list_list = attrs = []
        if str(cls.__name__) == "Rectangle":
            attrs = ['id', 'width', 'height', 'x', 'y']
        else:
            attrs = ['id', 'size', 'x', 'y']
        if not os.path.exists(filename):
            return list_list
        with open(filename, mode="r", encoding="utf-8") as a_file:
            csv_reader = csv.reader(a_file)
            for row in csv_reader:
                # convert row to dict
                dict_attrs = {attrs[i]: int(row[i]) for i in range(len(row))}
                list_list.append(dict_attrs)
        return [cls.create(**obj) for obj in list_list]
