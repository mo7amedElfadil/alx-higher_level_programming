#!/usr/bin/python3.8
"""Define MagicClass class"""

import math


class MagicClass:
    """definition of MagicClass class
    Args:
        radius: (int) Optional, 0 by default.

    Attributes:
        radius (int, private): radius of circle, 0 by default.

    """

    def __init__(self, radius=0):
        """instantiation of class
        Args:
            radius: (int) Optional, 0 by default.
        Attributes:
            radius (int, private): radius of circle, 0 by default.

        """
        self.__radius = 0
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """returns area of circle"""
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """returns circumference of circle"""
        return 2 * math.pi * self.__radius
