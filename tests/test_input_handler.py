import unittest
from src.utils.input_handler import parse_int
from src.utils.input_handler import parse_comma_sep_int_list
from src.utils.input_handler import parse_int_list

class TestInputHandler(unittest.TestCase):

    def test_parse_int(self):
        self.assertEqual(parse_int("10"), 10)
        self.assertEqual(parse_int("-2"), -2)
        self.assertEqual(parse_int("\n"), None)

    def test_comma_sep_int_file(self):
        file_contents = parse_comma_sep_int_list("../docs/testinputs/comma_sep_int.txt")
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(file_contents, expected)

    def test_int_list_file(self):
        file_contents = parse_int_list("../docs/testinputs/int_list.txt")
        expected = [1000, 5, 23, None, 3465, 2]
        self.assertEqual(file_contents, expected)

"""Test Suite Runner"""
if __name__ == '__main__':
    unittest.main()
