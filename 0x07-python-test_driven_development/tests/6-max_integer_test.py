#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_module_docstring(self):
        """Tests for module docsting"""
        mod_doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(mod_doc) > 1)

    def test_function_docstring(self):
        """Tests for function docstring"""
        fun_doc = max_integer.__doc__
        self.assertTrue(len(fun_doc) > 1)

    def testEmptyList(self):
        """Tests for getting an empty list"""
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([]), None)

    def testIfMax(self):
        """Tests for getting a correct list
        compare result to static ints
        """
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, -22, 3, 0]), 3)
        self.assertEqual(max_integer([0, -3]), 0)
        self.assertEqual(max_integer([1.3, 1, 0]), 1.3)

    def testCompareMax(self):
        """Tests for getting a correct list
        compare result to the max() function
        """
        self.assertEqual(max_integer([1]), max([1]))
        self.assertEqual(max_integer([1, -22, 3, 0]), max([1, -22, 3, 0]))
        self.assertEqual(max_integer([0, -3]), max([0, -3]))
        self.assertEqual(max_integer([1.3, 1, 0]), max([1.3, 1, 0]))

    def testLastMaxPositive(self):
        """Tests for all positive with max at end"""
        lst = [53, 12, 48, 236, 514, 5550]
        self.assertEqual(max_integer(lst), 5550)

    def testMidMaxPositive(self):
        """Tests for all positive with max in middle"""
        lst = [53, 12, 4856, 514, 550]
        self.assertEqual(max_integer(lst), 4856)

    def testFirstMaxPositive(self):
        """Tests for all positive with max at beginning"""
        lst = [4856, 12, 54, 514, 550]
        self.assertEqual(max_integer(lst), 4856)

    def testNegative(self):
        """Tests for list with one negative number"""
        lst = [486, 12, 54, 514, -550]
        self.assertEqual(max_integer(lst), 514)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        lst = [-486, -12, -54, -514, -550]
        self.assertEqual(max_integer(lst), -12)

    def testFail(self):
        """Tests when function fails
        first is test for no args"""
        self.assertIsNone(max_integer())
        with self.assertRaises(NameError):
            max_integer(x)
        with self.assertRaises(TypeError):
            max_integer(None)

    def testNotNumArg(self):
        """Tests for a non-numeric type in list"""
        lst = [4856, 12, "54", 514, 550]
        with self.assertRaises(TypeError):
            max_integer(lst)
