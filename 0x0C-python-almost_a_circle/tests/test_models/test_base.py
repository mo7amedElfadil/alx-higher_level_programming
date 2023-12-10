#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """unittest class for Base class"""
    def test_class_docstring(self):
        """test class documentation"""
        mod_doc = Base.__doc__
        self.assertTrue(len(mod_doc) > 1)

    def test_instance(self):
        """Test instance Creation"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_instance(self):
        """Test instance Creation"""
        b1 = Base()
        self.assertEqual(b1.id, 1)



# if __name__ == '__main__':
#     unittest.main()
