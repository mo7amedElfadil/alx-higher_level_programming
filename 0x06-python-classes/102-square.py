#!/usr/bin/python3
"""Define square class"""


class Square():
    """definition of Square class

    Args:
        size (int) Optional 0 by default.

    Attributes:
        size (int, private): size of square, 0 by default

    Methods:
        area (Public): returns area (int) of the instance square
        size(): property getter, returns size of square
        size(value): property setter, sets size attribute to value
            if value meets the requirements mentioned in method doc.

        """
    def __init__(self, size=0):
        """Function to initialize instance of Square with Optional
        attribute size(defaults to 0).

        """
        self.size = size

    @property
    def size(self):
        """getter for size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size property
             if size < 0 --> raise ValueError with
            msg : size must be >= 0.
            if size is not integer --> raise TypeError with
            msg : size must be an integer.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method that returns instance square area"""

        return self.__size ** 2

    """Defining private instance methods to answer comparators:
        ==, !=, >, >=, < and <=
        based on the square area
    """
    def __eq__(self, other):
        """private instance method for == comparator"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __lt__(self, other):
        """private instance method for < comparator"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        """private instance method for <= comparator"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()

    def __ne__(self, other):
        """private instance method for != comparator"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()

    def __gt__(self, other):
        """private instance method for > comparator"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        """private instance method for >= comparator"""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()


