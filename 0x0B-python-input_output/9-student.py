#!/usr/bin/python3
"""Defining 9-student module
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

    def to_json(self):
        """retrieves a dictionary representation of a student instance
        """
        return self.__dict__.copy()
