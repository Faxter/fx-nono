import unittest

from src.puzzle import Puzzle


class TestPuzzle(unittest.TestCase):
    def test_create_puzzle_from_dict(self):
        p = Puzzle(3, 2, [[1], [1], [1]], [[3], [1]])
        self.assertIsInstance(p, Puzzle)
        self.assertEqual(p.rows, 3)
        self.assertEqual(p.columns, 2)
        self.assertListEqual(p.row_hints, [[1], [1], [1]])
        self.assertListEqual(p.column_hints, [[3], [1]])

    def test_create_puzzle_invalid_rows(self):
        with self.assertRaises(ValueError):
            Puzzle(0, 2, [[1]], [[1]])

    def test_create_puzzle_invalid_columns(self):
        with self.assertRaises(ValueError):
            Puzzle(2, 0, [[1]], [[1]])

    def test_create_puzzle_invalid_row_hints(self):
        with self.assertRaises(ValueError):
            Puzzle(2, 3, [[1]], [[1], [1], [1]])

    def test_create_puzzle_invalid_column_hints(self):
        with self.assertRaises(ValueError):
            Puzzle(2, 3, [[1], [1]], [[1]])
