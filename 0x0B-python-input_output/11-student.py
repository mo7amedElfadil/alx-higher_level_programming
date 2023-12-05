#!/usr/bin/python3
"""Defining 11-student module
Contains class Student
"""


class Student:
    """Definition of Student class
        Attributes:
            first_name (public)
            last_name (public)
            age (public)

    """

    def __init__(self, first_name, last_name, age):
        """instatiate student instance with its attribs
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a student instance
        """
        if type(attrs) is list and all(type(s) is str for s in attrs):
            my_dict = {}
            for s in attrs:
                if s in self.__dict__:
                    my_dict[s] = self.__dict__[s]
            return my_dict
        return self.__dict__.copy()

    def reload_from_json(self, json):
        for key, val in json.items():
            self.__dict__[key] = val
