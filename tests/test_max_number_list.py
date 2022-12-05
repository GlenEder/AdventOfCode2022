import unittest
from src.utils.number_handlers.max_number_list import MaxNumberList

class TestMaxNumberList(unittest.TestCase):
    def test_init(self):
        maxList = MaxNumberList(5)
        self.assertEqual(maxList.length, 5)
        self.assertEqual(maxList.sum(), 0)

    def test_reinit(self):
        maxList = MaxNumberList(3)
        self.assertEqual(maxList.length, 3)
        self.assertEqual(maxList.sum(), 0)

        maxList.reinit([1, 2])
        self.assertEqual(maxList.length, 2)
        self.assertEqual(maxList.sum(), 3)

    def test_add(self):
        maxList = MaxNumberList(3)
        maxList.add(1)
        maxList.add(2)
        maxList.add(3)

        self.assertEqual(maxList.sum(), 6)

    def test_add_with_drop(self):
        maxList = MaxNumberList(3)
        maxList.add(1)
        maxList.add(2)
        maxList.add(3)
        maxList.add(4)

        self.assertEqual(maxList.sum(), 9)

    def test_add_without_drop(self):
        maxList = MaxNumberList(3)
        maxList.add(2)
        maxList.add(3)
        maxList.add(4)
        maxList.add(1)

        self.assertEqual(maxList.sum(), 9)

    def test_max(self):
        maxList = MaxNumberList(3)
        maxList.add(2)
        maxList.add(3)
        maxList.add(4)
        maxList.add(1)

        self.assertEqual(maxList.max(), 4)

"""Test Suite Runner"""
if __name__ == '__main__':
    unittest.main()
