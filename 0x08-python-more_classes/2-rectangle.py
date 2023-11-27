#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
    """Definition of Rectangle Class
        Args:
        width (int) Optional, 0 by default.
        height (int) Optional, 0 by default.

    Attributes:
        width (int, private): width of Rectangle, 0 by default.
        height (int, private): height of Rectangle, 0 by default.
    Methods:
        area (Public): returns area (int) of the instance Rectangle
        perimeter (Public): returns perimeter (int) of the instance Rectangle
        width: property setter and getter
        height: property setter and getter
            Args:
            value: value of width/height
            if value meets the requirements mentioned in method doc.
    """

    def __init__(self, width=0, height=0):
        """Function to initialize instance of Rectangle
        Attributes:
        width (int, private): width of Rectangle, 0 by default.
        height (int, private): height of Rectangle, 0 by default.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width property
             if width < 0 --> raise ValueError with
            msg : width must be >= 0.
            if width is not integer --> raise TypeError with
            msg : width must be an integer.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height property
             if height < 0 --> raise ValueError with
            msg : height must be >= 0.
            if height is not integer --> raise TypeError with
            msg : height must be an integer.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if 0 in [self.width, self.height]:
            return 0
        return 2 * (self.width + self.height)
