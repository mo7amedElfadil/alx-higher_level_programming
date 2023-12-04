#!/usr/bin/python3
"""Defining 10-square module
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Definition of Square Class
        Inherits from Rectangle Class
    """
    def __init__(self, size):
        """Instantiate the square instance with size.
        size is validated using the super() class's integer_validator
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns area of square
        """
        return self.__size ** 2

    def __str__(self):
        return f"[{Rectangle.__name__}] {self.__size:d}/{self.__size:d}"
