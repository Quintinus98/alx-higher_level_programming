#!/usr/bin/python3
"""Unit test for py models"""
import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """Unittests for base"""
    def test_default_id(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_without_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)


if __name__ == '__main__':
    unittest.main()
