import unittest

from src.cell_state import CellState
from src.grid import Grid, GridCoord


class TestGrid(unittest.TestCase):
    def test_create_coord(self):
        c = GridCoord(2, 3)
        self.assertIsInstance(c, GridCoord)
        self.assertEqual(c.column, 2)
        self.assertEqual(c.row, 3)

    def test_print_coord(self):
        c = GridCoord(2, 3)
        self.assertEqual(c.__repr__(), "2:3")

    def test_coord_equality(self):
        c1 = GridCoord(2, 3)
        c2 = GridCoord(2, 3)
        self.assertEqual(c1, c2)

    def test_coord_inequality(self):
        c1 = GridCoord(2, 3)
        c2 = GridCoord(1, 3)
        self.assertNotEqual(c1, c2)

    def test_hash_coord(self):
        c1 = GridCoord(2, 3)
        c2 = GridCoord(2, 3)
        self.assertEqual(hash(c1), hash(c2))

    def test_create_grid(self):
        rows = 7
        columns = 3
        g = Grid(rows, columns)
        self.assertIsInstance(g, Grid)
        self.assertEqual(len(g._grid), columns)
        self.assertEqual(len(g._grid[0]), rows)
        self.assertTrue(
            all(cell == CellState.UNKNOWN for col in g._grid for cell in col)
        )

    def test_fill(self):
        g = Grid(5, 10)
        g.fill(GridCoord(1, 2))
        self.assertEqual(g._grid[1][2], CellState.FULL)

    def test_clear(self):
        g = Grid(5, 10)
        g.clear(GridCoord(1, 2))
        self.assertEqual(g._grid[1][2], CellState.EMPTY)

    def test_maybe(self):
        g = Grid(5, 10)
        g.maybe(GridCoord(1, 2))
        self.assertEqual(g._grid[1][2], CellState.MAYBE)

    def test_reset(self):
        g = Grid(5, 10)
        g.reset(GridCoord(1, 2))
        self.assertEqual(g._grid[1][2], CellState.UNKNOWN)

    def test_is_cell_full(self):
        g = Grid(5, 10)
        g.fill(GridCoord(1, 1))
        self.assertTrue(g.is_cell_full(GridCoord(1, 1)))

    def test_is_cell_empty(self):
        g = Grid(5, 10)
        g.clear(GridCoord(1, 1))
        self.assertTrue(g.is_cell_empty(GridCoord(1, 1)))

    def test_is_cell_maybe(self):
        g = Grid(5, 10)
        g.maybe(GridCoord(1, 1))
        self.assertTrue(g.is_cell_maybe(GridCoord(1, 1)))

    def test_is_cell_unknown(self):
        g = Grid(5, 10)
        self.assertTrue(g.is_cell_unknown(GridCoord(1, 1)))

    def test_get_row(self):
        g = Grid(2, 3)
        g.fill(GridCoord(1, 0))
        row = g.get_row(0)
        self.assertListEqual(
            row, [CellState.UNKNOWN, CellState.FULL, CellState.UNKNOWN]
        )

    def test_get_column(self):
        g = Grid(2, 3)
        g.fill(GridCoord(0, 1))
        column = g.get_column(0)
        self.assertListEqual(column, [CellState.UNKNOWN, CellState.FULL])

    def test_is_complete(self):
        g = Grid(2, 3)
        g.fill(GridCoord(0, 0))
        g.fill(GridCoord(1, 0))
        g.clear(GridCoord(2, 0))
        g.clear(GridCoord(0, 1))
        g.fill(GridCoord(1, 1))
        g.fill(GridCoord(2, 1))
        self.assertTrue(g.is_complete())

    def test_is_complete_missing_cell(self):
        g = Grid(2, 3)
        g.fill(GridCoord(0, 0))
        g.fill(GridCoord(1, 0))
        g.clear(GridCoord(2, 0))
        g.clear(GridCoord(0, 1))
        g.fill(GridCoord(1, 1))
        self.assertFalse(g.is_complete())
