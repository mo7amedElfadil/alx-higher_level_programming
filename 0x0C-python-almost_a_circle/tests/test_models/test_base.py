#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models.base import Base
import inspect
import pep8
from models.rectangle import Rectangle
from models.square import Square


class TestBaseDocPep8(unittest.TestCase):
    """unittest class for Base class documentation and pep8 conformaty"""
    def test_pep8_base(self):
        """Test that the base module conforms to PEP8."""
        style = pep8.StyleGuide()
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_base(self):
        """Test that the test_base module conforms to PEP8."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """test class documentation"""
        import models.base as base
        mod_doc = base.__doc__
        self.assertTrue(len(mod_doc) > 0)

    def test_class_docstring(self):
        """test class documentation"""
        mod_doc = Base.__doc__
        self.assertTrue(len(mod_doc) > 0)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        base_funcs = inspect.getmembers(Base, inspect.isfunction)
        base_funcs.extend(inspect.getmembers(Base, inspect.ismethod))
        for func in base_funcs:
            self.assertTrue(len(func[1].__doc__) > 0)


class TestBaseClassWorking(unittest.TestCase):
    """unittest class for Base class when everything works"""

    def test_instance_no_id(self):
        """Test instance Creation with id none"""
        b1 = Base()
        my_id = 4
        self.assertIsInstance(b1, Base)
        self.assertEqual(b1.id, my_id)
        b2 = Base()
        self.assertEqual(b2.id, my_id + 1)

    def test_instance(self):
        """Test instance Creation with id none"""
        b1 = Base(2)
        self.assertIsInstance(b1, Base)
        self.assertEqual(b1.id, 2)

    def test_instance_id(self):
        """Test instance id assignment"""
        b1 = Base(3)
        self.assertEqual(b1.id, 3)
        b1.id = 6
        self.assertEqual(b1.id, 6)

    def test_multiple_instances(self):
        """Test multiple instance creations"""
        b1 = Base(3)
        b2 = Base(4)
        self.assertEqual([b1.id, b2.id], [3, 4])

    def test_to_json_str(self):
        """Test to_json_string method"""
        jstr = Base.to_json_string([{'x': 1, 'y': 9, 'id': 1,
                                   'height': 2, 'width': 10}])
        self.assertIsInstance(jstr, str)
        self.assertEqual(jstr, '[{"x": 1, "y": 9, "id": 1,'
                               ' "height": 2, "width": 10}]')

    def test_to_json_string_empty_str(self):
        """Test to_json_string empty str"""
        jstr = Base.to_json_string([])
        self.assertTrue(type(jstr) is str)
        self.assertEqual(jstr, "[]")

    def test_None_to_json_String(self):
        """Test to_json_string None"""
        jstr = Base.to_json_string(None)
        self.assertTrue(type(jstr) is str)
        self.assertEqual(jstr, "[]")

    def test_from_json_str(self):
        """Test from_json_string method"""
        b1 = Base()
        my_list = [{"x": 1, "y": 9, "id": 1, "height": 2, "width": 10}]
        jlist = b1.from_json_string('[{"x": 1, "y": 9, "id": 1,'
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
        jstr = Base.to_json_string(my_list)
        jlist = Base.from_json_string(jstr)
        self.assertIsInstance(jlist, list)
        self.assertIsInstance(jlist[0], dict)
        self.assertIsInstance(jlist[0]["x"], int)
        self.assertEqual(len(jlist), 2)
        self.assertEqual(len(jlist[0]), 5)
        self.assertEqual(len(jlist[1]), 5)
        self.assertEqual(jlist, my_list)
        self.assertEqual(jlist[0], my_list[0])
        self.assertEqual(jlist[1], my_list[1])

    def test_from_json_string_empty_str(self):
        """Test to_json_string empty str"""
        jlist = Base.from_json_string("")
        self.assertTrue(type(jlist) is list)
        self.assertEqual(jlist, [])

    def test_None_from_json_String(self):
        """Test to_json_string None"""
        jlist = Base.from_json_string(None)
        self.assertTrue(type(jlist) is list)
        self.assertEqual(jlist, [])

    def test_save_to_file(self):
        """Test save_to_file method"""
        from os.path import isfile
        my_list = [Rectangle(1, 1)]
        Rectangle.save_to_file(my_list)
        self.assertTrue(isfile(Rectangle.__name__ + ".json"))

    def test_save_to_file_csv(self):
        """Test save_to_file_csv method"""
        from os.path import isfile
        my_list = [Rectangle(1, 1)]
        Rectangle.save_to_file_csv(my_list)
        self.assertTrue(isfile(Rectangle.__name__ + ".csv"))

    def test_create_rect(self):
        """test create method for rectangle with incorrect value"""
        my_dict = {"x": 1, "s": 9, "id": 1, "height": 2, "width": 10}
        r1 = Rectangle.create(**my_dict)
        r2 = Rectangle(width=10, height=2, x=1, id=1)
        self.assertEqual(r1.__dict__, r2.__dict__)

    def test_create_square(self):
        """test create method for square with incorrect value"""
        my_dict = {"x": 1, "s": 9, "id": 1, "size": 2}
        s1 = Square.create(**my_dict)
        s2 = Square(size=2, x=1, id=1)
        self.assertEqual(s1.__dict__, s2.__dict__)


class TestBaseClassBreaking(unittest.TestCase):
    """unittest class for Base class when everything breaks"""

    def test_instance_too_many_args(self):
        """Test instance id assignment"""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_str_id(self):
        """Test multiple instance creations"""
        b1 = Base('A')
        self.assertEqual(b1.id, 'A')

    def test_nb_objects_private(self):
        b1 = Base(1)
        with self.assertRaises(AttributeError):
            b1.nb_objects
        with self.assertRaises(AttributeError):
            b1.__nb_objects
        self.assertFalse("nb_objects" in b1.__dict__)

    def test_no_arg_to_json_str(self):
        """Test for passing empty list"""
        jstr = Base.to_json_string([])
        self.assertIsInstance(jstr, str)
        self.assertEqual(jstr, "[]")

    def test_None_to_json_str(self):
        """Test for passing None"""
        jstr = Base.to_json_string(None)
        self.assertIsInstance(jstr, str)
        self.assertEqual(jstr, "[]")

    def test_from_json_str_empty_str(self):
        """Tests from_json_string with an empty string"""
        self.assertEqual([], Base.from_json_string(""))

    def test_from_json_str_None(self):
        """Tests from_json_string with None"""
        self.assertEqual([], Base.from_json_string(None))
