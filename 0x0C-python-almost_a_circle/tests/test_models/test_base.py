#!/usr/bin/python3
"""Unit test for py models"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch

class TestBaseMethods(unittest.TestCase):
    """Unittests for base"""
    def clear(self):
        Base._Base__nb_objects = 0

    def test_default_id(self):
        self.clear()
        a = Base()
        self.assertEqual(a.id, 1)
    
    def test_assign_id_prev(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    # def setUp(self):
    #     """ Method invoked for each test """
    #     Base._Base__nb_objects = 0

    def test_base_89(self):
        """ Test assigned id """
        new = Base(89)
        self.assertEqual(new.id, 89)

    def test_to_json_string_none(self):
        """ Test nb object attribute """
        b = Base()
        self.assertAlmostEqual(b.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        b = Base()
        self.assertAlmostEqual(b.to_json_string([]), "[]")

    def test_to_json_string(self):
        b = Base()
        self.assertTrue(b.to_json_string([ { 'id': 12 }]))

    def test_to_json_string_returns(self):
        b = Base()
        self.assertEqual(b.to_json_string([ { 'id': 12 }]), '[{"id": 12}]')

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string(self):
        self.assertTrue(Base.from_json_string('[{ "id": 89 }]'))

    def test_from_json_string_returns(self):
        self.assertTrue(Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])

    def test_more_args_id(self):
        """ Test passing more args to init method """
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        """ Test accessing to private attributes """
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file_1(self):
        """ Test JSON file """
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Test JSON file """
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")


if __name__ == '__main__':
    unittest.main()
