import unittest

from src.cell_state import CellState
from src.grid import Grid
from src.puzzle import Puzzle
from src.verifier import Verifier


class TestVerifier(unittest.TestCase):
    def setUp(self) -> None:
        rows = 6
        columns = 4
        self.grid = Grid(rows, columns)
        row_hints = [[3], [2], [1, 1], [2], [3], [1, 1]]
        col_hints = [[1, 1, 2], [1, 2], [6], [1]]
        self.puzzle = Puzzle(rows, columns, row_hints, col_hints)
        self.verifier = Verifier(self.puzzle, self.grid)

        # fill correctly
        self.grid.fill(0, 0)
        self.grid.fill(1, 0)
        self.grid.fill(2, 0)
        self.grid.clear(3, 0)
        self.grid.clear(0, 1)
        self.grid.clear(1, 1)
        self.grid.fill(2, 1)
        self.grid.fill(3, 1)
        self.grid.fill(0, 2)
        self.grid.clear(1, 2)
        self.grid.fill(2, 2)
        self.grid.clear(3, 2)
        self.grid.clear(0, 3)
        self.grid.fill(1, 3)
        self.grid.fill(2, 3)
        self.grid.clear(3, 3)
        self.grid.fill(0, 4)
        self.grid.fill(1, 4)
        self.grid.fill(2, 4)
        self.grid.clear(3, 4)
        self.grid.fill(0, 5)
        self.grid.clear(1, 5)
        self.grid.fill(2, 5)
        self.grid.clear(3, 5)

    def test_create_verifier(self):
        self.assertIsInstance(self.verifier, Verifier)

    def test_verify_line_one_block(self):
        self.assertTrue(
            self.verifier.verify_line(self.puzzle.row_hints[0], self.grid.get_row(0))
        )

    def test_verify_line_multiple_blocks(self):
        self.assertTrue(
            self.verifier.verify_line(self.puzzle.column_hints[0], self.grid._grid[0])
        )

    def test_verify_empty_line(self):
        self.assertTrue(
            self.verifier.verify_line(
                [], [CellState.EMPTY, CellState.EMPTY, CellState.EMPTY]
            )
        )

    def test_verify_error_block_amount(self):
        self.grid.clear(1, 0)
        self.assertFalse(
            self.verifier.verify_line(self.puzzle.row_hints[0], self.grid.get_row(0))
        )

    def test_verify_error_block_length(self):
        self.grid.clear(0, 0)
        self.assertFalse(
            self.verifier.verify_line(self.puzzle.row_hints[0], self.grid.get_row(0))
        )

    def test_verify_correct(self):
        self.assertTrue(self.verifier.verify())

    def test_verify_column_error(self):
        self.grid.clear(3, 1)
        self.grid.fill(1, 1)
        self.assertFalse(self.verifier.verify())

    def test_verify_row_error(self):
        self.grid.clear(3, 1)
        self.grid.fill(3, 2)
        self.assertFalse(self.verifier.verify())
