#!/usr/bin/python3
"""square module. Contains class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class. Inherits from Rectangle

    Attributes:
        __nb_objects (private, class attribute): default 0
        id (public, instance attribute): default None
        width (private, instance attribute)
        height (private, instance attribute)
        x (private, instance attribute): default 0
        y (private, instance attribute): default 0

    Methods:
        width: property getter, and setter
        height: property getter, and setter
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialize id attrib for this class and any that inherits from it.
        Args:
            id (public, instance attribute): Optional, default None
            width (private, instance attribute)
            height (private, instance attribute)
            x (private, instance attribute): Optional, default 0
            y (private, instance attribute): Optional, default 0

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """returns print representation of Square's attributes"""
        return f"[{Square.__name__}] ({self.id})"\
            f" {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute using *args and **kwargs
        """
        attribs = ['id', 'size', 'x', 'y']
        for i, arg in enumerate(args):
            if i < len(attribs):
                setattr(self, attribs[i], arg)
        if args:
            return
        for k, v in kwargs.items():
            if k in attribs:
                setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Square
        """

        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
