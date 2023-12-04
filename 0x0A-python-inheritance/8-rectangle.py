#!/usr/bin/python3
"""Defining 8-rectangle module
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
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height


