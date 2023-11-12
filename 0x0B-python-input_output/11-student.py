#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """Represents a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if (type(attrs) is list and
                all(type(elem) is str for elem in attrs)):
            return ({key: getattr(self, key)
                    for key in attrs if hasattr(self, key)})
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for k in json:
            try:
                setattr(self, k, json[k])
            except FileNotFoundError:
                pass
