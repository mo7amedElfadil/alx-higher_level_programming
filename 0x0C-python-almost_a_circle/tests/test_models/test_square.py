#!/usr/bin/python3
"""Unittest for Rectangle class
"""
import unittest
from models.base import Base
import inspect
import pep8
from models.rectangle import Rectangle
from models.square import Square
from contextlib import redirect_stdout as RS
import io
from io import StringIO as SIO
from os.path import isfile


class TestSquareDocPep8(unittest.TestCase):
    """unittest class for Square class documentation and pep8 conformaty"""
    def test_pep8_square(self):
        """Test that the square module conforms to PEP8."""
        style = pep8.StyleGuide()
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_square(self):
        """Test that the test_square module conforms to PEP8."""
        style = pep8.StyleGuide()
        result = style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """test class documentation"""
        import models.square as square
        mod_doc = square.__doc__
        self.assertTrue(len(mod_doc) > 0)

    def test_class_docstring(self):
        """test class documentation"""
        mod_doc = Square.__doc__
        self.assertTrue(len(mod_doc) > 0)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        square_funcs = inspect.getmembers(Square, inspect.isfunction)
        square_funcs.extend(inspect.getmembers(Square, inspect.ismethod))
        for func in square_funcs:
            if func:
                self.assertTrue(len(func[1].__doc__) > 0)


class TestSquareClassWorking(unittest.TestCase):
    """unittest class for Square class when everything works"""
    @classmethod
    def setUpClass(cls):
        """Set up a couple of instances that will be used multiple times"""
        cls.s1 = Square(10, 0, 0, 1)
        cls.s2 = Square(10, 0, 0, 12)
        cls.default = Square(1, 0, 0, 1)

    def test_instance(self):
        """Test instance Creation with id none"""
        s1 = Square(10, id=12)
        self.assertIsInstance(s1, Square)
        self.assertEqual(s1.id, 12)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_instance_kwargs(self):
        """Test instance Creation with id none"""
        s1 = Square(id=10, size=10, x=0, y=12)
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 12)

    def test_instance_id(self):
        """Test instance id assignment"""
        s1 = self.s2
        self.assertEqual(s1.id, 12)
        s1.id = 6
        self.assertEqual(s1.id, 6)
        self.s2.id = 12

    def test_multiple_instances(self):
        """Test multiple instance creations"""
        s1 = self.s1
        s2 = self.s2
        s3 = Square(1)
        s4 = Square(2)
        self.assertEqual([s1.id, s2.id], [1, 12])
        self.assertEqual([s3.id, s4.id], [25, 26])

    def test_square_area(self):
        """Test area"""
        s1 = Square(10)
        s2 = Square(5)
        self.assertEqual(s1.area(), 10 ** 2)
        self.assertEqual(s2.area(), 5 ** 2)

    def test_square_print(self):
        """Test print"""
        s1 = self.s1
        with RS(SIO()) as f:
            print(s1, end="")
        self.assertEqual(f.getvalue(), str(s1))
        self.assertEqual(f.getvalue(), "[Square] (1) 0/0 - 10")

    def test_update_args(self):
        """Testing the udpate method with *args and str representation
        order if args is -> ['id', 'size', 'x', 'y']
        """
        s1 = Square(1, 0, 0, 1)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 1")
        s1.update(89)
        self.assertEqual(str(s1), "[Square] (89) 0/0 - 1")
        s1.update(89, 2)
        self.assertEqual(str(s1), "[Square] (89) 0/0 - 2")
        s1.update(89, 2, 3)
        self.assertEqual(str(s1), "[Square] (89) 3/0 - 2")
        s1.update(89, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (89) 3/4 - 2")

    def test_update_too_many_args(self):
        """test too many args for update"""
        s1 = self.default
        s1.update(99, 7, 7, 8, 100)
        self.assertEqual(str(s1), "[Square] (99) 7/8 - 7")

    def test_update_kwargs(self):
        """Testing the udpate method with **kwargs and str representation
        order of args is -> ['id', 'size', 'x', 'y']
        """
        s1 = Square(size=1, x=0, y=0, id=1)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 1")
        s1.update(id=89)
        self.assertEqual(str(s1), "[Square] (89) 0/0 - 1")
        s1.update(id=89, size=2)
        self.assertEqual(str(s1), "[Square] (89) 0/0 - 2")
        s1.update(id=89, size=3)
        self.assertEqual(str(s1), "[Square] (89) 0/0 - 3")
        s1.update(x=89, size=3, id=4)
        self.assertEqual(str(s1), "[Square] (4) 89/0 - 3")
        s1.update(id=89, size=2, x=4, y=5)
        self.assertEqual(str(s1), "[Square] (89) 4/5 - 2")

    def test_update_too_many_kwargs(self):
        """test too many kwargs for update"""
        s1 = self.default
        s1.update(id=1, size=2, x=4, y=5, s=99)
        self.assertEqual(str(s1), "[Square] (1) 4/5 - 2")

    def test_update_no_args(self):
        """test no args for update"""
        s1 = Square(1, 0, 0, 1)
        s1.update()
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 1")

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        my_dict = {"x": 0, "y": 0, "id": 1, "size": 1}
        jdict = self.default.to_dictionary()
        self.assertIsInstance(jdict, dict)
        self.assertIsInstance(jdict["size"], int)
        self.assertEqual(len(jdict), len(my_dict))
        self.assertEqual(jdict, my_dict)
        self.assertTrue(type(jdict) is dict)
        self.assertEqual(str(self.default), str(Square.create(**jdict)))

    def test_square_display(self):
        """Test display"""
        s1 = Square(2)
        s2 = Square(1)
        with RS(SIO()) as f:
            s1.display()
        self.assertEqual(f.getvalue(), '##\n##\n')
        with RS(SIO()) as f:
            s2.display()
        self.assertEqual(f.getvalue(), '#\n')

    def test_to_json_str(self):
        """Test to_json_string method"""
        jstr = Square.to_json_string([{'x': 1, 'y': 9, 'id': 1,
                                       'size': 10}])
        self.assertIsInstance(jstr, str)
        self.assertEqual(jstr, '[{"x": 1, "y": 9, "id": 1,'
                               ' "size": 10}]')

    def test_from_json_str(self):
        """Test from_json_string method"""
        my_list = [{"x": 1, "y": 9, "id": 1, "size": 10}]
        jlist = Square.from_json_string('[{"x": 1, "y": 9, "id": 1,'
                                        ' "size": 10}]')
        self.assertIsInstance(jlist, list)
        self.assertIsInstance(jlist[0], dict)
        self.assertIsInstance(jlist[0]["x"], int)
        self.assertEqual(len(jlist), 1)
        self.assertEqual(len(jlist[0]), 4)
        self.assertEqual(jlist, my_list)

    def test_from_json_str_multi_dict_list(self):
        """Test from_json_string method with mutiple dictionaries
        and different order"""
        my_list = [{"x": 1, "y": 9, "id": 1, "size": 10},
                   {"x": 2, "size": 10, "id": 1, "y": 8}]
        jstr = Square.to_json_string(my_list)
        jlist = Square.from_json_string(jstr)
        self.assertIsInstance(jlist, list)
        self.assertIsInstance(jlist[0], dict)
        self.assertIsInstance(jlist[0]["x"], int)
        self.assertEqual(len(jlist), 2)
        self.assertEqual(len(jlist[0]), 4)
        self.assertEqual(len(jlist[1]), 4)
        self.assertEqual(jlist, my_list)
        self.assertEqual(jlist[0], my_list[0])
        self.assertEqual(jlist[1], my_list[1])

    def test_save_to_file(self):
        """Test save_to_file method"""
        from json import loads
        my_list = [self.s1]
        Square.save_to_file(my_list)
        self.assertTrue(isfile(Square.__name__ + ".json"))
        with open(Square.__name__ + ".json", "r") as file:
            self.assertEqual(loads(file.read()), [self.s1.to_dictionary()])

    def test_save_to_file_None(self):
        """Test save_to_file method with None"""
        from json import loads
        Square.save_to_file(None)
        self.assertTrue(isfile(Square.__name__ + ".json"))
        with open(Square.__name__ + ".json", "r") as file:
            self.assertEqual(loads(file.read()), [])

    def test_save_to_file_empty_list(self):
        """Test save_to_file method with empty list"""
        from json import loads
        Square.save_to_file([])
        self.assertTrue(isfile(Square.__name__ + ".json"))
        with open(Square.__name__ + ".json", "r") as file:
            self.assertEqual(loads(file.read()), [])

    def test_load_from_file(self):
        """Test load_from_file method"""
        from json import loads
        my_list = [self.s1, self.s2]
        Square.save_to_file(my_list)
        list_squares_output = Square.load_from_file()
        self.assertTrue(isfile(Square.__name__ + ".json"))
        self.assertEqual(len(my_list), len(list_squares_output))
        for inp, out in zip(my_list, list_squares_output):
            self.assertIsInstance(inp, Square)
            self.assertIsInstance(out, Square)
            self.assertEqual(str(inp), str(out))

    def test_save_to_file_csv(self):
        """Test save_to_file_csv method"""
        my_list = [self.s1, self.s2]
        Square.save_to_file_csv(my_list)
        self.assertTrue(isfile(Square.__name__ + ".csv"))

    def test_load_from_file_csv(self):
        """Test load_from_file_csv method"""
        my_list = [self.s1, self.s2]
        Square.save_to_file_csv(my_list)
        self.assertTrue(isfile(Square.__name__ + ".csv"))
        csv_loaded = Square.load_from_file_csv()
        self.assertEqual(len(my_list), len(csv_loaded))
        for inp, out in zip(my_list, csv_loaded):
            self.assertIsInstance(inp, Square)
            self.assertIsInstance(out, Square)
            self.assertEqual(str(inp), str(out))

    def test_create_square(self):
        """test create method for square with incorrect value"""
        my_dict = {"x": 1, "s": 9, "id": 1, "size": 2}
        s1 = Square.create(**my_dict)
        self.assertTrue(type(s1) is Square)
        s2 = Square(size=2, x=1, id=1)
        self.assertEqual(s1.__dict__, s2.__dict__)
        self.assertIsInstance(s1, Square)


class TestSquareClassBreaking(unittest.TestCase):
    """unittest class for Square class when everything breaks"""
    @classmethod
    def setUpClass(cls):
        """Set up a couple of instances that will be used multiple times"""
        cls.s1 = Square(10, 0, 0, 1)
        cls.s2 = Square(10, 0, 0, 12)
        cls.default = Square(1, 0, 0, 1)

    def test_instance_too_little_args(self):
        """Test instance id assignment"""
        with self.assertRaises(TypeError):
            Square()

    def test_str_id(self):
        """Test multiple instance creations"""
        s1 = Square(3, id='A')
        self.assertEqual(s1.id, 'A')

    def test_wrong_size(self):
        """Test instance Creation with wrong size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(id=10, size=0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(id=10, size=None)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(id=10, size=-10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(id=10, size='0')
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(id=10, size=[0])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(id=10, size=True)
        with self.assertRaises(TypeError):
            Square(id=10)

    def test_wrong_x(self):
        """Test instance Creation with wrong x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(id=10, size=2, x=-1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(id=10, size=10, x='0')
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(id=10, size=1, x=None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(id=10, size=1, x=False)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(id=10, size=10, x=[1])

    def test_wrong_y(self):
        """Test instance Creation with wrong y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(id=10, size=2, y=-1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(id=10, size=10, y='0')
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(id=10, size=1, y=None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(id=10, size=1, y=True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(id=10, size=10, y=[1])

    def test_update_incorrect_args(self):
        """Testing the udpate method with incorrect *args
        order if args is -> ['id', 'size', 'x', 'y']
        """
        s1 = self.default
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(89, -2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(89, False)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(89, 2, '4')
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.update(89, 2, -4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(89, 2, 4, [5])
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.update(89, 2, 4, -5)

    def test_update_incorrect_kwargs(self):
        """Testing the udpate method with incorrect **kwargs
        order if args is -> ['id', 'width', 'height', 'x', 'y']
        """
        s1 = Square(size=1, x=0, y=0, id=1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(id=89, size=-2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(id=89, size='2')
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(x='89', size=3, id=4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.update(x=-89, size=3, id=4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(id=89, size=2, x=4, y=None)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.update(id=89, size=2, x=4, y=-5)

    def test_display_with_arg(self):
        """Test display with too many args (should be none)"""
        with self.assertRaises(TypeError):
            self.s1.display(1)

    def test_rectangle_area_failing(self):
        """Test area"""
        s1 = self.default
        with self.assertRaises(TypeError):
            s1.area(1)

    def test_nb_objects_private(self):
        s1 = self.s1
        with self.assertRaises(AttributeError):
            s1.nb_objects
        with self.assertRaises(AttributeError):
            s1.__nb_objects
        self.assertFalse("nb_objects" in s1.__dict__)

    def test_no_arg_to_json_str(self):
        """Test for passing empty list"""
        jstr = Square.to_json_string([])
        self.assertIsInstance(jstr, str)
        self.assertEqual(jstr, "[]")

    def test_None_to_json_str(self):
        """Test for passing None"""
        jstr = Square.to_json_string(None)
        self.assertIsInstance(jstr, str)
        self.assertEqual(jstr, "[]")

        """Tests from_json_string with an empty string"""
        self.assertEqual([], Square.from_json_string(""))

    def test_from_json_str_None(self):
        """Tests from_json_string with None"""
        self.assertEqual([], Square.from_json_string(None))
