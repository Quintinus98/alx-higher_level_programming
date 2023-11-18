#!/usr/bin/python3
""" Module for test Rectangle class """
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    """ Suite to test Rectangle class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_rectangle_temp_rectangle(self):
        """ Test temp rectangle """
        temp = Rectangle(1, 1)
        self.assertEqual(temp.width, 1)
        self.assertEqual(temp.height, 1)
        self.assertEqual(temp.x, 0)
        self.assertEqual(temp.y, 0)
        self.assertEqual(temp.id, 1)

    def test_rectangle_temp_rectangle_2(self):
        """ Test temp rectangle with all params """
        temp = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(temp.width, 2)
        self.assertEqual(temp.height, 3)
        self.assertEqual(temp.x, 5)
        self.assertEqual(temp.y, 5)
        self.assertEqual(temp.id, 4)

    def test_rectangle_temp_rectangles(self):
        """ Test temp rectangles """
        temp = Rectangle(1, 1)
        temp2 = Rectangle(1, 1)
        self.assertEqual(False, temp is temp2)
        self.assertEqual(False, temp.id == temp2.id)

    def test_rectangle_is_Base_instance(self):
        """ Test Rectangle is a Base instance """
        temp = Rectangle(1, 1)
        self.assertEqual(True, isinstance(temp, Base))

    def test_rectangle_incorrect_amount_params(self):
        """ Test error raise with 1 arg passed """
        with self.assertRaises(TypeError):
            temp = Rectangle(1)

    def test_rectangle_incorrect_amount_params_1(self):
        """ Test error raised with no args passed """
        with self.assertRaises(TypeError):
            temp = Rectangle()

    def test_rectangle_access_private_params(self):
        """ Trying to access to a private attribute """
        temp = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            temp.__width

    def test_rectangle_access_private_params_2(self):
        """ Trying to access to a private attribute """
        temp = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            temp.__height

    def test_rectangle_access_private_params_3(self):
        """ Trying to access to a private attribute """
        temp = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            temp.__x

    def test_rectangle_access_private_params_4(self):
        """ Trying to access to a private attribute """
        temp = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            temp.__y

    def test_rectangle_valide_params(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            temp = Rectangle("2", 2, 2, 2, 2)

    def test_rectangle_valide_params_2(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            temp = Rectangle(2, "2", 2, 2, 2)

    def test_rectangle_valide_params_3(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            temp = Rectangle(2, 2, "2", 2, 2)

    def test_rectangle_valide_params_4(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            temp = Rectangle(2, 2, 2, "2", 2)

    def test_rectangle_value_params(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            temp = Rectangle(0, 1)

    def test_rectangle_value_params_1(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            temp = Rectangle(1, 0)

    def test_rectangle_value_params_2(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            temp = Rectangle(1, 1, -1)

    def test_rectangle_value_params_3(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            temp = Rectangle(1, 1, 1, -1)

    def test_rectangle_area(self):
        """ Checking the return value of area method """
        temp = Rectangle(4, 5)
        self.assertEqual(temp.area(), 20)

    def test_rectangle_area_2(self):
        """ Checking the return value of area method """
        temp = Rectangle(2, 2)
        self.assertEqual(temp.area(), 4)
        temp.width = 5
        self.assertEqual(temp.area(), 10)
        temp.height = 5
        self.assertEqual(temp.area(), 25)

    def test_rectangle_area_3(self):
        """ Checking the return value of area method """
        temp = Rectangle(3, 8)
        self.assertEqual(temp.area(), 24)
        temp2 = Rectangle(10, 10)
        self.assertEqual(temp2.area(), 100)

    def test_rectangle_display(self):
        """ Test string printed """
        r1 = Rectangle(2, 5)
        res = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_rectangle_display_2(self):
        """ Test string printed """
        r1 = Rectangle(2, 2)
        res = "##\n##\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.width = 5
        res = "#####\n#####\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_rectangle_str(self):
        """ Test __str__ return value """
        r1 = Rectangle(2, 5, 2, 4)
        res = "[Rectangle] (1) 2/4 - 2/5\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_rectangle_str_2(self):
        """ Test __str__ return value """
        r1 = Rectangle(3, 2, 8, 8, 10)
        res = "[Rectangle] (10) 8/8 - 3/2\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r1.id = 2
        r1.width = 7
        r1.height = 15
        res = "[Rectangle] (2) 8/8 - 7/15\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_rectangle_str_3(self):
        """ Test __str__ return value """
        r1 = Rectangle(5, 10)
        res = "[Rectangle] (1) 0/0 - 5/10\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(25, 86, 4, 7)
        res = "[Rectangle] (2) 4/7 - 25/86\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r3 = Rectangle(1, 1, 1, 1)
        res = "[Rectangle] (3) 1/1 - 1/1\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            print(r3)
            self.assertEqual(str_out.getvalue(), res)

    def test_rectangle_str_4(self):
        """ Test __str__ return value """
        r1 = Rectangle(3, 3)
        res = "[Rectangle] (1) 0/0 - 3/3"
        self.assertEqual(r1.__str__(), res)

    def test_rectangle_display_3(self):
        """ Test string printed """
        r1 = Rectangle(5, 4, 1, 1)
        res = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_rectangle_display_4(self):
        """ Test string printed """
        r1 = Rectangle(3, 2)
        res = "###\n###\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.x = 4
        res = "    ###\n    ###\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.y = 2
        res = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_rectangle_to_dictionary(self):
        """ Test dictionary returned """
        r1 = Rectangle(1, 2, 3, 4, 1)
        res = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', temp=StringIO()) as str_out:
            print(type(r1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_rectangle_to_dictionary_2(self):
        """ Test dictionary returned """
        r1 = Rectangle(2, 2, 2, 2)
        res = "[Rectangle] (1) 2/2 - 2/2\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(5, 7)
        res = "[Rectangle] (2) 0/0 - 5/7\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', temp=StringIO()) as str_out:
            print(type(r1_dictionary))
            self.assertEqual(str_out.getvalue(), res)

    def test_rectangle_dict_to_json(self):
        """ Test Dictionary to JSON string """
        r1 = Rectangle(2, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', temp=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_rectangle_check_value(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

    def test_rectangle_check_value_2(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)

    def test_rectangle_create(self):
        """ Test create method """
        dictionary = {'id': 89}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)

    def test_rectangle_create_2(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_rectangle_create_3(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_rectangle_create_4(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

    def test_rectangle_create_5(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_rectangle_load_from_file(self):
        """ Test load JSON file """
        load_file = Rectangle.load_from_file()
        self.assertEqual(load_file, [])

    def test_rectangle_load_from_file_2(self):
        """ Test load JSON file """
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        linput = [r1, r2]
        Rectangle.save_to_file(linput)
        loutput = Rectangle.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())
