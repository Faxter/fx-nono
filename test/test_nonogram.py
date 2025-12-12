import unittest

from src.cell_state import CellState
from src.grid import GridCoord
from src.nonogram import Nonogram, verify_line
from src.puzzle import Puzzle


class TestNonogram(unittest.TestCase):
    def setUp(self) -> None:
        rows = 6
        columns = 4
        row_hints = [[3], [2], [1, 1], [2], [3], [1, 1]]
        col_hints = [[1, 1, 2], [1, 2], [6], [1]]
        self.nonogram = Nonogram(Puzzle(rows, columns, row_hints, col_hints))
        self.nonogram.grid.fill(GridCoord(0, 0))
        self.nonogram.grid.fill(GridCoord(1, 0))
        self.nonogram.grid.fill(GridCoord(2, 0))
        self.nonogram.grid.clear(GridCoord(3, 0))
        self.nonogram.grid.clear(GridCoord(0, 1))
        self.nonogram.grid.clear(GridCoord(1, 1))
        self.nonogram.grid.fill(GridCoord(2, 1))
        self.nonogram.grid.fill(GridCoord(3, 1))
        self.nonogram.grid.fill(GridCoord(0, 2))
        self.nonogram.grid.clear(GridCoord(1, 2))
        self.nonogram.grid.fill(GridCoord(2, 2))
        self.nonogram.grid.clear(GridCoord(3, 2))
        self.nonogram.grid.clear(GridCoord(0, 3))
        self.nonogram.grid.fill(GridCoord(1, 3))
        self.nonogram.grid.fill(GridCoord(2, 3))
        self.nonogram.grid.clear(GridCoord(3, 3))
        self.nonogram.grid.fill(GridCoord(0, 4))
        self.nonogram.grid.fill(GridCoord(1, 4))
        self.nonogram.grid.fill(GridCoord(2, 4))
        self.nonogram.grid.clear(GridCoord(3, 4))
        self.nonogram.grid.fill(GridCoord(0, 5))
        self.nonogram.grid.clear(GridCoord(1, 5))
        self.nonogram.grid.fill(GridCoord(2, 5))
        self.nonogram.grid.clear(GridCoord(3, 5))

    def test_create_nonogram(self):
        n = Nonogram(Puzzle(3, 2, [[1], [1], [1]], [[3], [1]]))
        self.assertIsInstance(n, Nonogram)
        self.assertEqual(n.grid.rows, 3)
        self.assertEqual(n.grid.columns, 2)

    def test_verify_line_one_block(self):
        self.assertTrue(
            verify_line(
                self.nonogram.puzzle.row_hints[0], self.nonogram.grid.get_row(0)
            )
        )

    def test_verify_line_multiple_blocks(self):
        self.assertTrue(
            verify_line(
                self.nonogram.puzzle.column_hints[0], self.nonogram.grid._grid[0]
            )
        )

    def test_verify_empty_line(self):
        self.assertTrue(
            verify_line([], [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY])
        )

    def test_verify_error_block_amount(self):
        self.nonogram.grid.clear(GridCoord(1, 0))
        self.assertFalse(
            verify_line(
                self.nonogram.puzzle.row_hints[0], self.nonogram.grid.get_row(0)
            )
        )

    def test_verify_error_block_length(self):
        self.nonogram.grid.clear(GridCoord(0, 0))
        self.assertFalse(
            verify_line(
                self.nonogram.puzzle.row_hints[0], self.nonogram.grid.get_row(0)
            )
        )

    def test_verify_correct(self):
        self.assertTrue(self.nonogram.verify())

    def test_verify_column_error(self):
        self.nonogram.grid.clear(GridCoord(3, 1))
        self.nonogram.grid.fill(GridCoord(1, 1))
        self.assertFalse(self.nonogram.verify())

    def test_verify_row_error(self):
        self.nonogram.grid.clear(GridCoord(3, 1))
        self.nonogram.grid.fill(GridCoord(3, 2))
        self.assertFalse(self.nonogram.verify())
