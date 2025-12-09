import unittest

from src.nonogram import Nonogram
from src.puzzle import parse_puzzle


class TestNonogram(unittest.TestCase):
    def test_create_nonogram(self):
        n = Nonogram(parse_puzzle({"rows": 3, "columns": 4}))
        self.assertIsInstance(n, Nonogram)
        self.assertEqual(n.grid.rows, 3)
        self.assertEqual(n.grid.columns, 4)
