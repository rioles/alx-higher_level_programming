#!/usr/bin/python3
# test_base.py

"""Define unittest for base.py"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing intantiation of the Base class."""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_no_arg(self):
        """Test for constructor of base with None argument passed"""
        b_01 = Base(None)
        self.assertEqual(b_01.id, 1)

    def test_two_arg(self):
        """Test for constructor of base with None argument passed"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b2.id, 2)

    def test_multiple_instance(self):
        """Test for constructor of base with  argument passed or None"""
        b1 = Base()
        b2 = Base()
        b3 = Base(11)
        b4 = Base(-20)
        b5 = Base(float("-inf"))
        b6 = Base(0)
        b7 = Base(1.1)
        b8 = Base()
        self.assertEqual(b1.id, b2 - 1)
        self.assertEqual(b2.id, b8 - 2)
        self.assertEqual(b3.id, 11)
        self.assertEqual(b4.id, -12)
        self.assertEqual(b5.id, float("-inf"))
        self.assertEqual(b6.id, 0)
        self.assertEqual(b7.id, 1.1)
        self.assertEqual(b8.id, 3)

    def test_multiple_instance_with_id(self):
        """Test for multiple instance creation with id"""
        b1 = Base(3)
        b2 = Base(4)
        self.assertEqual(b1.id, 3)
        self.assertEqual(b2.id, 4)

    def test_for_string(self):
        """Test for string argument"""
        b1 = Base("foo")
        self.assertEqual(b1.id, "foo")

    def test_for_same_id(self):
        """Test for same ids"""
        b1 = Base(22)
        self.assertEqual(b1.id, 22)
        b2 = Base(22)
        self.assertEqual(b2.id, 22)

if __name__=='__main__':
    unittest.main()
