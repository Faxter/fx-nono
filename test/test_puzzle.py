import unittest

from src.puzzle import Puzzle, parse_puzzle


class TestPuzzle(unittest.TestCase):
    def test_create_puzzle_from_dict(self):
        d = {"rows": 5, "columns": 10}
        puzzle = parse_puzzle(d)
        self.assertIsInstance(puzzle, Puzzle)
        self.assertEqual(puzzle.rows, 5)
        self.assertEqual(puzzle.columns, 10)
