import unittest
import sys
from io import StringIO
from src.days.day3 import day3
from utils.io_handlers.input_handler import get_test_input_filepath
from utils.io_handlers.output_handler import get_day_info


class TestDay3(unittest.TestCase):
    def test_day3(self):
        # save std out to reset later
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            day3(get_test_input_filepath(3))
            output = out.getvalue().strip()
            expected = get_day_info(3, 157, 70)
            self.assertEqual(output, expected)
        finally:
            sys.stdout = saved_stdout


if __name__ == '__main__':
    unittest.main()
