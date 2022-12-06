import unittest
import sys
from io import StringIO
from src.days.day2 import day2
from utils.io_handlers.input_handler import get_test_input_filepath
from utils.io_handlers.output_handler import get_day_info


class TestDay2(unittest.TestCase):
    def test_day2(self):
        # save std out to reset later
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            day2(get_test_input_filepath(2))
            output = out.getvalue().strip()
            expected = get_day_info(2, 15, 12)
            self.assertEqual(output, expected)
        finally:
            sys.stdout = saved_stdout


if __name__ == '__main__':
    unittest.main()
