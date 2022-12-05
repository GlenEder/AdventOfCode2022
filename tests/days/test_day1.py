import unittest
import sys
from io import StringIO
from src.days.day1 import day1
from utils.io_handlers.input_handler import get_test_input_filepath
from utils.io_handlers.output_handler import get_day_info


class TestDay1(unittest.TestCase):
    def test_day1(self):
        # save std out to reset later
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            day1(get_test_input_filepath(1))
            output = out.getvalue().strip()
            expected = get_day_info(1, 24000, 45000)
            self.assertEqual(output, expected)
        finally:
            sys.stdout = saved_stdout


if __name__ == '__main__':
    unittest.main()
