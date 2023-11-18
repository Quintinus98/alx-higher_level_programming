#!/usr/bin/python3
"""Unit test for py models"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import os


class TestSquareMethods(unittest.TestCase):
    def test_square_1(self):
        """Test of Square(1) exists"""
        self.assertTrue(Square(1))

    def test_square_1_2(self):
        """Test of Square(1, 2) exists"""
        self.assertTrue(Square(1, 2))

    def test_square_1_2_3(self):
        """Test of Square(1, 2, 3) exists"""
        self.assertTrue(Square(1, 2, 3))

    def test_square_str1(self):
        """Test of Square("1") exists"""
        with self.assertRaises(TypeError) as err:
            Square("1")
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_square_1_str2(self):
        """Test of Square(1, "2") exists"""
        with self.assertRaises(TypeError) as err:
            Square(1, "2")

    def test_square_1_2_str3(self):
        """Test of Square(1, 2, "3") exists"""
        with self.assertRaises(TypeError) as err:
            Square(1, 2, "3")

    def test_square_1_2_3_4(self):
        """Test of Square(1, 2, 3, 4) exists"""
        self.assertTrue(Square(1, 2, 3, 4))

    def test_square_neg_1(self):
        """Test of Square(-1) exists"""
        with self.assertRaises(ValueError) as err:
            Square(-1)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_square_1_neg_2(self):
        """Test of Square(1, -2) exists"""
        with self.assertRaises(ValueError) as err:
            Square(1, -2)
        self.assertEqual(str(err.exception), "x must be >= 0")

    def test_square_1_2_neg_3(self):
        """Test of Square(1, 2, -3) exists"""
        with self.assertRaises(ValueError) as err:
            Square(1, 2, -3)
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_square_0(self):
        """Test of Square(0) exists"""
        with self.assertRaises(ValueError) as err:
            Square(0)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_square__str__(self):
        """Test of __str__() for Square exists"""
        s1 = Square(1, 2, 3, 4)
        res = "[Square] (4) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_square_to_dictionary(self):
        """Test of to_dictionary() in Square exists"""
        s1 = Square(10, 2, 1, 1)
        s1_dictionary = s1.to_dictionary()
        res = "{'id': 1, 'size': 10, 'x': 2, 'y': 1}\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1_dictionary)
            self.assertEqual(str_out.getvalue(), res)

    def test_square_update(self):
        """Test of update() in Square exists"""
        s1 = Square(10, 2, 1, 2)
        self.assertFalse(s1.update())

    def test_square_update_89(self):
        """Test of update(89) in Square exists"""
        s1 = Square(10, 2, 1, 2)
        s1.update(89)
        res = "[Square] (89) 2/1 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_square_update_89_1(self):
        """Test of update() in Square exists"""
        s1 = Square(10, 2, 1, 2)
        s1.update(89, 1)
        res = "[Square] (89) 2/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_square_update_89_1_2(self):
        """Test of update() in Square exists"""
        s1 = Square(10, 3, 1, 2)
        s1.update(89, 1, 2)
        res = "[Square] (89) 2/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_square_update_89_1_2_3(self):
        """Test of update() in Square exists"""
        s1 = Square(10, 3, 1, 2)
        s1.update(89, 1, 2, 3)
        res = "[Square] (89) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_square_update_id(self):
        """Test of update(**{ 'id': 89 }) in Square exists"""
        s1 = Square(10, 2, 1, 2)
        s1.update(**{'id': 89})
        res = "[Square] (89) 2/1 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_square_update_id_size(self):
        """Test of update(**{'id': 89, 'size': 1}) in Square exists"""
        s1 = Square(10, 2, 1, 2)
        s1.update(**{'id': 89, 'size': 1})
        res = "[Square] (89) 2/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_square_update_id_size_x(self):
        """
            Test of update(**{ 'id': 89, 'size': 1, 'x': 2 })
            in Square exists
        """
        s1 = Square(10, 3, 1, 2)
        s1.update(**{'id': 89, 'size': 1, 'x': 2})
        res = "[Square] (89) 2/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_square_update_id_size_x_y(self):
        """
            Test ofupdate(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
            in Square exists
        """
        s1 = Square(10, 3, 1, 2)
        s1.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        res = "[Square] (89) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_square_create_id(self):
        """Test of create(**{ 'id': 89 }) in Square exists"""
        s1 = Square.create(**{'id': 89})
        res = "[Square] (89) 0/0 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_square_create_id_size(self):
        """Test of create(**{ 'id': 89, 'size': 1 }) in Square exists"""
        s1 = Square.create(**{'id': 89, 'size': 1})
        res = "[Square] (89) 0/0 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_square_create_id_size_x(self):
        """
            Test of create(**{ 'id': 89, 'size': 1, 'x': 2 })
            in Square exists
        """
        s1 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        res = "[Square] (89) 2/0 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_square_create_id_size_x_y(self):
        """
            Test of create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
            in Square exists
        """
        s1 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        res = "[Square] (89) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), res)

    def test_square_save_to_file_none(self):
        """Test of Square.save_to_file(None) in Square exists"""
        Square.save_to_file(None)
        with open("Square.json", "r") as a_file:
            self.assertTrue(len(a_file.read()) == 2)

    def test_square_save_to_file_empty(self):
        """Test of Square.save_to_file([]) in Square exists"""
        Square.save_to_file([])
        with open("Square.json", "r") as a_file:
            self.assertTrue(len(a_file.read()) == 2)

    def test_square_save_to_file_size(self):
        """Test of Square.save_to_file([Square(1)]) in Square exists"""
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as a_file:
            self.assertTrue(len(a_file.read()) > 2)

    def test_square_load_from_file_exists(self):
        """Test of Square.load_from_file() when file exist exists"""
        Square.save_to_file([Square(1)])
        self.assertTrue(Square.load_from_file())

    def test_square_load_from_file(self):
        """Test of Square.load_from_file() when file doesn’t exist exists"""
        try:
            os.remove("Square.json")
        except IOError:
            pass
        self.assertEqual(Square.load_from_file(), [])


if __name__ == "__main__":
    unittest.main()
