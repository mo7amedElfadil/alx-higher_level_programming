#!/usr/bin/python3
"""Defining 9-rectangle module
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Definition of Rectangle Class
        Inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """Instantiate the rectangle instance with width and height.
        width and height validated
        Using the super() class's integer_validator
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[{Rectangle.__name__}] {self.__width:d}/{self.__height:d}"
