#!/usr/bin/python3
# 2-square.py
"""Define square class"""


class Square():
    """definition of Square class

    Args:
        size (int) Optional 0 by default.
            if size is not integer --> raise TypeError with
            msg : size must be an integer.
            if size < 0 --> raise ValueError with
            msg : size must be >= 0.

    Attributes:
        size (int, private): size of square, 0 by default

        """
    def __init__(self, size=0):
        """Function to initialize square's Optional attrib size(defaults to 0).
            if size is not integer --> raise TypeError with
            msg : size must be an integer.
            if size < 0 --> raise ValueError with
            msg : size must be >= 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
