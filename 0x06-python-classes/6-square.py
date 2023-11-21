#!/usr/bin/python3
"""Define square class"""
class Square():
    """definition of Square class
    Args:
        size (int) Optional, 0 by default.
        position (tuple): Optional, (0, 0) by default.

    Attributes:
        size (int, private): size of square, 0 by default.
        position (tuple, private): position of square, (0, 0) by default.

    Methods:
        area (Public): returns area (int) of the instance square
        size: property getter, returns size of square
        size: property setter, sets size attribute to value
            Args: 
            value: value of size
            if value meets the requirements mentioned in method doc.
        position: property getter, returns position tuple of square
        position: property setter, sets position attribute to value
        myprint: Public instance method that prints a size x size square using '#' characters
                    if size == 0 just prints a newline
                    Offsets square by value of position

        """


    def __init__(self, size = 0, position = (0, 0)):
        """Function to initialize instance of Square with Optional 
        Attributes:
            size (int, private): size of square, 0 by default.
            position (tuple, private): position of square, (0, 0) by default.

        """
        self.size = size
        self.position = position


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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    @property
    def position(self):
        """getter for position property"""
        return self.__position


    @position.setter
    def position(self, value):
        """setter for size property
             if size < 0 --> raise ValueError with 
            msg : size must be >= 0.
            if size is not integer --> raise TypeError with
            msg : size must be an integer.

        """
        if (not isinstance(value, tuple) or
        len(value) != 2 or
        not all(isinstance(v, int) for v in value) or
        not all(v >= 0 for v in value)):
                    raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


    def area(self):
        """Public instance method that returns instance square area"""
        return self.__size ** 2


    def my_print(self):
        """Public instance method that prints a size x size square using '#' characters
                if size == 0 just prints a newline
            Offsets square by value of position
        """
        if (self.__size == 0):
            print()
        print("\n"*self.__position[1], end ="")
        for i in range(self.__size):
            print(" "*self.__position[0] + "#"*self.__size)

