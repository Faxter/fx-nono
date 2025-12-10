import unittest

from src.nonogram import Nonogram
from src.puzzle import Puzzle


class TestNonogram(unittest.TestCase):
    def test_create_nonogram(self):
        n = Nonogram(Puzzle(3, 2, [[1], [1], [1]], [[3], [1]]))
        self.assertIsInstance(n, Nonogram)
        self.assertEqual(n.grid.rows, 3)
        self.assertEqual(n.grid.columns, 2)
