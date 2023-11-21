#!/usr/bin/python3
# 1-square.py
""" Define a class square with a private attribute size."""


class Square():
    """ definition of square class

    Args:
        size (int): size of square

    Attributes:
        size (int, private): size of square
    """
    def __init__(self, size):
        """Initialize square class and set size value"""
        self.__size = size
