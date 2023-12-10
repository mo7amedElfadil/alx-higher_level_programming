#!/usr/bin/python3
"""rectangle module. Contains class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class. Inherits from Base

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

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize id attrib for this class and any that inherits from it.
        Args:
            id (public, instance attribute): Optional, default None
            width (private, instance attribute)
            height (private, instance attribute)
            x (private, instance attribute): Optional, default 0
            y (private, instance attribute): Optional, default 0

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public instance method that returns instance rectangle area"""
        return self.width * self.height

    def display(self):
        """prints representation of Rectangle using '#' character"""
        result = []
        if 0 in [self.width, self.height]:
            print()
        if self.y:
            result.append("\n" * (self.y - 1))
        for _ in range(self.height):
            result.append(" "*self.x + "#"*self.width)
        print("\n".join(result))

    def __str__(self):
        """returns print representation of Rectangle's attributes"""
        return f"[{Rectangle.__name__}] ({self.id})"\
            f" {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute using *args and **kwargs
        """
        attribs = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            setattr(self, attribs[i], arg)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle
        """

        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }



if __name__ == "__main__":
    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
