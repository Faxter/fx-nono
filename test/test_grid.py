import unittest

from src.cell_state import CellState
from src.grid import Grid


class TestGrid(unittest.TestCase):
    def test_create_grid(self):
        rows = 7
        columns = 3
        g = Grid(rows, columns)
        self.assertIsInstance(g, Grid)
        self.assertEqual(len(g._grid), columns)
        self.assertEqual(len(g._grid[0]), rows)
        self.assertTrue(all(cell == CellState.UNKNOWN for col in g._grid for cell in col))

    def test_fill(self):
        g = Grid(5, 10)
        g.fill(1, 2)
        self.assertEqual(g._grid[1][2], CellState.FULL)

    def test_clear(self):
        g = Grid(5, 10)
        g.clear(1, 2)
        self.assertEqual(g._grid[1][2], CellState.EMPTY)

    def test_maybe(self):
        g = Grid(5, 10)
        g.maybe(1, 2)
        self.assertEqual(g._grid[1][2], CellState.MAYBE)

    def test_reset(self):
        g = Grid(5, 10)
        g.reset(1, 2)
        self.assertEqual(g._grid[1][2], CellState.UNKNOWN)

    def test_is_cell_full(self):
        g = Grid(5, 10)
        g.fill(1, 1)
        self.assertTrue(g.is_cell_full(1, 1))

    def test_is_cell_empty(self):
        g = Grid(5, 10)
        g.clear(1, 1)
        self.assertTrue(g.is_cell_empty(1, 1))

    def test_is_cell_maybe(self):
        g = Grid(5, 10)
        g.maybe(1, 1)
        self.assertTrue(g.is_cell_maybe(1, 1))

    def test_is_cell_unknown(self):
        g = Grid(5, 10)
        self.assertTrue(g.is_cell_unknown(1, 1))
