#!/usr/bin/python3
"""Unit test for py models"""
import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    def test_default_id(self):
        b = Base()
        self.assertEqual(b.id, 1)


if __name__ == '__main__':
    unittest.main()
