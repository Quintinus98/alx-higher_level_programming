"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit test for Max integer"""
    def test_module_doc(self):
        """Tests that the module doc exists"""
        self.assertTrue(len(__import__('5-text_indentation').__doc__) > 1)

    def test_func_doc(self):
        """Tests that the function doc exists"""
        f = len(max_integer.__doc__)
        self.assertTrue(f > 1)

    def test_max_end(self):
        """Tests that the max integer is correct when located at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_beginning(self):
        """Tests that the max integer is
            correct when located at the beginning"""
        self.assertEqual(max_integer([4, 3, 1, 2]), 4)

    def test_max_middle(self):
        """Tests that the max integer is
            correct when located in the middle"""
        self.assertEqual(max_integer([1, 4, 5, 3, 2]), 5)

    def test_negative_num(self):
        """Tests that the max integer is
            correct when a negative number is present"""
        self.assertEqual(max_integer([1, 4, -5, 3, 2]), 4)

    def test_only_negative_nums(self):
        """Tests that the max integer is
            correct when all numbers are negative"""
        self.assertEqual(max_integer([-1, -4, -5, -3]), -1)

    def test_one_elem_only(self):
        """Tests that the max integer is
            correct when there's only one number"""
        self.assertEqual(max_integer([99]), 99)

    def test_empty_list(self):
        """Tests that the max integer returns
            false when the list is empty"""
        self.assertFalse(max_integer())

    def test_str_in_list(self):
        """Tests that the max integer raises a
            TypeError if there is a string"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "name", 5])


if __name__ == "__main__":
    unittest.main()
