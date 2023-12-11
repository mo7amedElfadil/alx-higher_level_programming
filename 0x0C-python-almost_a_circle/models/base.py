#!/usr/bin/python3
"""base module. Contains class Base
"""


class Base:
    """Base class

    Attributes:
        __nb_objects (private, class attribute): default 0
        id (public, instance attribute): default None

    Methods:

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize id attrib for this class and any that inherits from it.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries
        """
        from json import dumps
        if list_dictionaries is None:
            return "[]"
        return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        """
        from json import loads
        if json_string is None or json_string == "[]" or\
                json_string == "":
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        """
        from json import dump
        res = []
        with open(f"{cls.__name__}.json", "w") as f:
            for obj in list_objs:
                res.append(obj.to_dictionary())

            f.write(cls.to_json_string(res))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        """
        """
        {"a" : 3}
        {"a" : 3, "width" , "height", }
        """
        attribs = ['width', 'height']
        if dictionary and len(dictionary) > 0:
            if (cls.__name__ == "Rectangle" and len(dictionary) > 1 and
                    all(x in dictionary.keys() for x in attribs)):
                inst = cls(1, 1)
            elif (cls.__name__ == "Square" and len(dictionary) > 0 and
                    "size" in dictionary.keys()):
                inst = cls(1)
            else:
                return
            inst.update(**dictionary)
            return inst

    @classmethod
    def load_from_file(cls):
        """save instance serialization to CSV
        format:
            Rectangle: <id>,<width>,<height>,<x>,<y>
            Square: <id>,<size>,<x>,<y>
        """

        res = []
        try:
            with open(f"{cls.__name__}.json", "r") as f:
                for line in f:
                    try:
                        for item in cls.from_json_string(line):
                            res.append(cls.create(**item))
                    except Exception:
                        pass
        except IOError:
            pass
        return res

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save instance serialization to CSV
        format:
            Rectangle: <id>,<width>,<height>,<x>,<y>
            Square: <id>,<size>,<x>,<y>
        """
        from csv import DictWriter as dw
        with open(f"{cls.__name__}.csv", "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
                return
            if cls.__name__ == "Rectangle":
                header = ["id", "width", "height", "x", "y"]
            else:
                header = ["id", "size", "x", "y"]
            cw = dw(f, fieldnames=header)
            cw.writeheader()

            for obj in list_objs:
                cw.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """load instance serialization from CSV (deserialization)
        format:
            Rectangle: <id>,<width>,<height>,<x>,<y>
            Square: <id>,<size>,<x>,<y>
        """
        from csv import DictReader as dr
        res = []
        try:
            with open(f"{cls.__name__}.csv", "r", newline="") as f:
                cr = dr(f, restval=int)
                for row in cr:
                    for k in row:
                        row[k] = int(row[k])
                    res.append(cls.create(**row))
        except IOError:
            pass
        return res

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw shape using turtle module"""
        import turtle
        from random import choice

        no_colors = 8

        colors = ["#"+''.join([choice('0123456789ABCDEF') for j in range(6)])
                  for i in range(no_colors)]
        T = turtle.Turtle()
        T.getscreen().bgcolor("#"+''.join([choice('0123456789ABCDEF')
                                           for j in range(6)]))
        T.speed(3)
        T.shape("turtle")
        T.pensize(2)
        for rect in list_rectangles:
            T.showturtle()
            c1 = choice(colors)
            T.color("white", c1)
            T.setpos(rect.x, rect.y)
            T.begin_fill()
            T.pendown()
            T.forward(rect.width)
            T.setheading(90)

            T.forward(rect.height)
            T.setheading(180)

            T.forward(rect.width)
            T.setheading(270)

            T.forward(rect.height)
            T.setheading(0)
            T.end_fill()
            T.penup()
            T.hideturtle()

        T.getscreen().bgcolor("#"+''.join([choice('0123456789ABCDEF')
                                           for j in range(6)]))
        for sq in list_squares:
            T.showturtle()
            c1 = choice(colors)
            T.color("white", c1)
            T.setpos(sq.x, sq.y)
            T.begin_fill()
            T.pendown()
            T.forward(sq.size)
            T.setheading(90)

            T.forward(sq.size)
            T.setheading(180)

            T.forward(sq.size)
            T.setheading(270)

            T.forward(sq.size)
            T.setheading(0)
            T.end_fill()
            T.penup()
            T.hideturtle()

        turtle.exitonclick()
