#!/usr/bin/python3
"""Define square class"""


class Square():
    """definition of Square class

    Args:
        size (int) Optional 0 by default.
            if size < 0 --> raise ValueError with
            msg : size must be >= 0.
            if size is not integer --> raise TypeError with
            msg : size must be an integer.

    Attributes:
        size (int, private): size of square, 0 by default

    Methods:
        area (Public): returns area (int) of the instance square

        """
    def __init__(self, size=0):
        """Function to initialize instance of Square with Optional
        attribute size(defaults to 0).
            if size < 0 --> raise ValueError with
            msg : size must be >= 0.
            if size is not integer --> raise TypeError with
            msg : size must be an integer.

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method that returns instance square area
        """
        return self.__size ** 2
