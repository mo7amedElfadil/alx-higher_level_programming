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


class TestRectangleDocPep8(unittest.TestCase):
    """unittest class for Rectangle class documentation and pep8 conformaty"""
    def test_pep8_rectangle(self):
        """Test that the rectangle module conforms to PEP8."""
        style = pep8.StyleGuide()
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_rectangle(self):
        """Test that the test_rectangle module conforms to PEP8."""
        style = pep8.StyleGuide()
        result = style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """test class documentation"""
        import models.rectangle as rectangle
        mod_doc = rectangle.__doc__
        self.assertTrue(len(mod_doc) > 0)

    def test_class_docstring(self):
        """test class documentation"""
        mod_doc = Rectangle.__doc__
        self.assertTrue(len(mod_doc) > 0)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        rectangle_funcs = inspect.getmembers(Rectangle, inspect.isfunction)
        rectangle_funcs.extend(inspect.getmembers(Rectangle, inspect.ismethod))
        for func in rectangle_funcs:
            if func:
                self.assertTrue(len(func[1].__doc__) > 0)


class TestRectangleClassWorking(unittest.TestCase):
    """unittest class for Rectangle class when everything works"""
    @classmethod
    def setUpClass(cls):
        """Set up a couple of instances that will be used multiple times"""
        cls.r1 = Rectangle(10, 2, 0, 0, 1)
        cls.r2 = Rectangle(10, 2, 0, 0, 12)
        cls.default = Rectangle(1, 1, 0, 0, 1)

    def test_instance(self):
        """Test instance Creation with id none"""
        r1 = Rectangle(10, 2, id=12)
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_instance_kwargs(self):
        """Test instance Creation with id none"""
        r1 = Rectangle(id=10, height=2, width=10, x=0, y=12)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 12)

    def test_instance_id(self):
        """Test instance id assignment"""
        r1 = self.r2
        self.assertEqual(r1.id, 12)
        r1.id = 6
        self.assertEqual(r1.id, 6)
        self.r2.id = 12

    def test_multiple_instances(self):
        """Test multiple instance creations"""
        r1 = self.r1
        r2 = self.r2
        r3 = Rectangle(1, 1)
        r4 = Rectangle(1, 2)
        self.assertEqual([r1.id, r2.id], [1, 12])
        self.assertEqual([r3.id, r4.id], [15, 16])

    def test_rectangle_area(self):
        """Test area"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(5, 7)
        self.assertEqual(r1.area(), 10 * 2)
        self.assertEqual(r2.area(), 5 * 7)

    def test_rectangle_print(self):
        """Test print"""
        r1 = self.r1
        with RS(SIO()) as f:
            print(r1, end="")
        self.assertEqual(f.getvalue(), str(r1))
        self.assertEqual(f.getvalue(), "[Rectangle] (1) 0/0 - 10/2")

    def test_update_args(self):
        """Testing the udpate method with *args and str representation
        order if args is -> ['id', 'width', 'height', 'x', 'y']
        """
        r1 = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 1/1")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 0/0 - 1/1")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 0/0 - 2/1")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 0/0 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/0 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_too_many_args(self):
        """test too many args for update"""
        r1 = self.default
        r1.update(7, 7, 7, 7, 7, 99)
        self.assertEqual(str(r1), "[Rectangle] (7) 7/7 - 7/7")

    def test_update_kwargs(self):
        """Testing the udpate method with **kwargs and str representation
        order if args is -> ['id', 'width', 'height', 'x', 'y']
        """
        r1 = Rectangle(width=1, height=1, x=0, y=0, id=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 1/1")
        r1.update(id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 0/0 - 1/1")
        r1.update(id=89, width=2)
        self.assertEqual(str(r1), "[Rectangle] (89) 0/0 - 2/1")
        r1.update(id=89, height=2, width=3)
        self.assertEqual(str(r1), "[Rectangle] (89) 0/0 - 3/2")
        r1.update(x=89, height=2, width=3, id=4)
        self.assertEqual(str(r1), "[Rectangle] (4) 89/0 - 3/2")
        r1.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_too_many_kwargs(self):
        """test too many kwargs for update"""
        r1 = self.default
        r1.update(id=1, width=2, height=3, x=4, y=5, s=99)
        self.assertEqual(str(r1), "[Rectangle] (1) 4/5 - 2/3")

    def test_update_no_args(self):
        """test no args for update"""
        r1 = Rectangle(1, 1, 0, 0, 1)
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 1/1")

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        my_dict = {"x": 0, "y": 0, "id": 1, "height": 1, "width": 1}
        jdict = self.default.to_dictionary()
        self.assertIsInstance(jdict, dict)
        self.assertIsInstance(jdict["height"], int)
        self.assertEqual(len(jdict), len(my_dict))
        self.assertEqual(jdict, my_dict)
        self.assertTrue(type(jdict) is dict)
        self.assertEqual(str(self.default), str(Rectangle.create(**jdict)))

    def test_display(self):
        """Test display"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(1, 1)
        with RS(SIO()) as f:
            r1.display()
        self.assertEqual(f.getvalue(), '###\n###\n')
        with RS(SIO()) as f:
            r2.display()
        self.assertEqual(f.getvalue(), '#\n')

    def test_to_json_str(self):
        """Test to_json_string method"""
        jstr = Rectangle.to_json_string([{'x': 1, 'y': 9, 'id': 1,
                                          'height': 2, 'width': 10}])
        self.assertIsInstance(jstr, str)
        self.assertEqual(jstr, '[{"x": 1, "y": 9, "id": 1,'
                               ' "height": 2, "width": 10}]')

    def test_from_json_str(self):
        """Test from_json_string method"""
        my_list = [{"x": 1, "y": 9, "id": 1, "height": 2, "width": 10}]
        jlist = Rectangle.from_json_string('[{"x": 1, "y": 9, "id": 1,'
                                           ' "height": 2, "width": 10}]')
        self.assertIsInstance(jlist, list)
        self.assertIsInstance(jlist[0], dict)
        self.assertIsInstance(jlist[0]["x"], int)
        self.assertEqual(len(jlist), 1)
        self.assertEqual(len(jlist[0]), 5)
        self.assertEqual(jlist, my_list)

    def test_from_json_str_multi_dict_list(self):
        """Test from_json_string method with mutiple dictionaries
        and different order"""
        my_list = [{"x": 1, "y": 9, "id": 1, "height": 2, "width": 10},
                   {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        jstr = Rectangle.to_json_string(my_list)
        jlist = Rectangle.from_json_string(jstr)
        self.assertIsInstance(jlist, list)
        self.assertIsInstance(jlist[0], dict)
        self.assertIsInstance(jlist[0]["x"], int)
        self.assertEqual(len(jlist), 2)
        self.assertEqual(len(jlist[0]), 5)
        self.assertEqual(len(jlist[1]), 5)
        self.assertEqual(jlist, my_list)
        self.assertEqual(jlist[0], my_list[0])
        self.assertEqual(jlist[1], my_list[1])

    def test_save_to_file(self):
        """Test save_to_file method"""
        from json import loads
        my_list = [self.r1]
        Rectangle.save_to_file(my_list)
        self.assertTrue(isfile(Rectangle.__name__ + ".json"))
        with open(Rectangle.__name__ + ".json", "r") as file:
            self.assertEqual(loads(file.read()), [self.r1.to_dictionary()])

    def test_save_to_file_none(self):
        """Test save_to_file method with none"""
        from json import loads
        Rectangle.save_to_file(None)
        self.assertTrue(isfile(Rectangle.__name__ + ".json"))
        with open(Rectangle.__name__ + ".json", "r") as file:
            self.assertEqual(loads(file.read()), [])

    def test_save_to_file_empty_list(self):
        """Test save_to_file method with empty list"""
        from json import loads
        Rectangle.save_to_file([])
        self.assertTrue(isfile(Rectangle.__name__ + ".json"))
        with open(Rectangle.__name__ + ".json", "r") as file:
            self.assertEqual(loads(file.read()), [])

    def test_load_from_file(self):
        """Test load_from_file method"""
        from json import loads
        my_list = [self.r1, self.r2]
        Rectangle.save_to_file(my_list)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertTrue(isfile(Rectangle.__name__ + ".json"))
        self.assertEqual(len(my_list), len(list_rectangles_output))
        for inp, out in zip(my_list, list_rectangles_output):
            self.assertIsInstance(inp, Rectangle)
            self.assertIsInstance(out, Rectangle)
            self.assertEqual(str(inp), str(out))

    def test_save_to_file_csv(self):
        """Test save_to_file_csv method"""
        my_list = [self.r1, self.r2]
        Rectangle.save_to_file_csv(my_list)
        self.assertTrue(isfile(Rectangle.__name__ + ".csv"))

    def test_load_from_file_csv(self):
        """Test load_from_file_csv method"""
        my_list = [self.r1, self.r2]
        Rectangle.save_to_file_csv(my_list)
        self.assertTrue(isfile(Rectangle.__name__ + ".csv"))
        csv_loaded = Rectangle.load_from_file_csv()
        self.assertEqual(len(my_list), len(csv_loaded))
        for inp, out in zip(my_list, csv_loaded):
            self.assertIsInstance(inp, Rectangle)
            self.assertIsInstance(out, Rectangle)
            self.assertEqual(str(inp), str(out))

    def test_create_rect(self):
        """test create method for rectangle with incorrect value"""
        my_dict = {"x": 1, "s": 9, "id": 1, "height": 2, "width": 10}
        r1 = Rectangle.create(**my_dict)
        self.assertTrue(type(r1) is Rectangle)
        r2 = Rectangle(width=10, height=2, x=1, id=1)
        self.assertEqual(r1.__dict__, r2.__dict__)
        self.assertIsInstance(r1, Rectangle)


class TestRectangleClassBreaking(unittest.TestCase):
    """unittest class for Rectangle class when everything breaks"""
    @classmethod
    def setUpClass(cls):
        """Set up a couple of instances that will be used multiple times"""
        cls.r1 = Rectangle(10, 2, 0, 0, 1)
        cls.r2 = Rectangle(10, 2, 0, 0, 12)
        cls.default = Rectangle(1, 1, 0, 0, 1)

    def test_instance_too_little_args(self):
        """Test instance id assignment"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_str_id(self):
        """Test multiple instance creations"""
        r1 = Rectangle(3, 3, id='A')
        self.assertEqual(r1.id, 'A')

    def test_wrong_width(self):
        """Test instance Creation with wrong width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(id=10, height=2, width=0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(id=10, height=2, width=None)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(id=10, height=2, width=-10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(id=10, height=2, width='0')
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(id=10, height=2, width=[0])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(id=10, height=2, width=True)
        with self.assertRaises(TypeError):
            Rectangle(id=10, height=2)

    def test_wrong_height(self):
        """Test instance Creation with wrong height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(id=10, height=0, width=2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(id=10, height=None, width=2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(id=10, height=-2, width=10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(id=10, height='2', width=1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(id=10, height=[2], width=10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(id=10, height=False, width=10)
        with self.assertRaises(TypeError):
            Rectangle(id=10, width=2)

    def test_wrong_x(self):
        """Test instance Creation with wrong x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(id=10, height=2, width=2, x=-1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(id=10, height=2, width=10, x='0')
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(id=10, height=2, width=1, x=None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(id=10, height=2, width=1, x=False)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(id=10, height=2, width=10, x=[1])

    def test_wrong_y(self):
        """Test instance Creation with wrong y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(id=10, height=2, width=2, y=-1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(id=10, height=2, width=10, y='0')
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(id=10, height=2, width=1, y=None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(id=10, height=2, width=1, y=True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(id=10, height=2, width=10, y=[1])

    def test_update_incorrect_args(self):
        """Testing the udpate method with incorrect *args
        order if args is -> ['id', 'width', 'height', 'x', 'y']
        """
        r1 = self.default
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(89, -2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(89, False)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(89, 2, -3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(89, 2, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(89, 2, 3, '4')
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(89, 2, 3, -4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(89, 2, 3, 4, [5])
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(89, 2, 3, 4, -5)

    def test_update_incorrect_kwargs(self):
        """Testing the udpate method with incorrect **kwargs
        order if args is -> ['id', 'width', 'height', 'x', 'y']
        """
        r1 = Rectangle(width=1, height=1, x=0, y=0, id=1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(id=89, width=-2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(id=89, width='2')
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(id=89, height=-2, width=3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(id=89, height='2', width=3)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(x='89', height=2, width=3, id=4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(x=-89, height=2, width=3, id=4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(id=89, width=2, height=3, x=4, y=None)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(id=89, width=2, height=3, x=4, y=-5)

    def test_display_with_arg(self):
        """Test display with too many args (should be none)"""
        with self.assertRaises(TypeError):
            self.r1.display(1)

    def test_rectangle_area_failing(self):
        """Test area"""
        r1 = self.default
        with self.assertRaises(TypeError):
            r1.area(1)

    def test_nb_objects_private(self):
        r1 = self.r1
        with self.assertRaises(AttributeError):
            r1.nb_objects
        with self.assertRaises(AttributeError):
            r1.__nb_objects
        self.assertFalse("nb_objects" in r1.__dict__)

    def test_no_arg_to_json_str(self):
        """Test for passing empty list"""
        jstr = Rectangle.to_json_string([])
        self.assertIsInstance(jstr, str)
        self.assertEqual(jstr, "[]")

    def test_None_to_json_str(self):
        """Test for passing None"""
        jstr = Rectangle.to_json_string(None)
        self.assertIsInstance(jstr, str)
        self.assertEqual(jstr, "[]")

        """Tests from_json_string with an empty string"""
        self.assertEqual([], Rectangle.from_json_string(""))

    def test_from_json_str_None(self):
        """Tests from_json_string with None"""
        self.assertEqual([], Rectangle.from_json_string(None))
