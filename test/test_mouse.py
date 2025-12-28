import unittest

from src.grid import GridCoord
from src.nonogram import Nonogram
from src.puzzle import Puzzle
from src.ui.layout import Layout
from src.ui.mouse import MouseController


class TestMouseController(unittest.TestCase):
    def setUp(self):
        """
        MMM (menu)
        _HH (col hints)
        Hxx (row hints + cells)
        Hxx
        Hxx
        """
        n = Nonogram(Puzzle(3, 2, [[1], [1], [1]], [[1], [1]]))
        self.layout = Layout(n)
        self.mouse_controller = MouseController(self.layout, 20)

    def test_create_mouse_controller(self):
        self.assertIsInstance(self.mouse_controller, MouseController)

    def test_handle_left_mouse_down_on_grid(self):
        self.mouse_controller.handle_mouse_down(1, (24, 52))
        self.assertTrue(self.layout.nonogram.grid.is_cell_full(GridCoord(0, 0)))

    def test_handle_left_mouse_down_on_grid_twice(self):
        self.mouse_controller.handle_mouse_down(1, (24, 52))
        self.mouse_controller.handle_mouse_down(1, (24, 52))
        self.assertTrue(self.layout.nonogram.grid.is_cell_unknown(GridCoord(0, 0)))

    def test_handle_middle_mouse_down_on_grid(self):
        self.mouse_controller.handle_mouse_down(2, (24, 52))
        self.assertTrue(self.layout.nonogram.grid.is_cell_maybe(GridCoord(0, 0)))

    def test_handle_right_mouse_down_on_grid(self):
        self.mouse_controller.handle_mouse_down(3, (24, 52))
        self.assertTrue(self.layout.nonogram.grid.is_cell_empty(GridCoord(0, 0)))

    def test_handle_other_mouse_down_on_grid(self):
        self.mouse_controller.handle_mouse_down(4, (24, 52))
        self.assertTrue(self.layout.nonogram.grid.is_cell_full(GridCoord(0, 0)))

    def test_handle_left_mouse_down_on_top_hint(self):
        self.mouse_controller.handle_mouse_down(1, (31, 34))
        self.assertTrue(self.layout.nonogram.puzzle.column_hints[0][0].crossed)

    def test_handle_left_mouse_down_on_left_hint(self):
        self.mouse_controller.handle_mouse_down(1, (2, 58))
        self.assertTrue(self.layout.nonogram.puzzle.row_hints[0][0].crossed)

    def test_handle_mouse_movement_without_dragging(self):
        self.mouse_controller.handle_mouse_position((29, 55))
        self.assertTrue(self.layout.nonogram.grid.is_cell_unknown(GridCoord(0, 0)))

    def test_handle_mouse_movement_while_dragging(self):
        self.mouse_controller.handle_mouse_down(1, (0, 0))
        self.mouse_controller.handle_mouse_position((29, 55))
        self.assertTrue(self.layout.nonogram.grid.is_cell_full(GridCoord(0, 0)))

    def test_handle_mouse_movement_after_dragging(self):
        self.mouse_controller.handle_mouse_down(1, (0, 0))
        self.mouse_controller.handle_mouse_up(1, (0, 0), [])
        self.mouse_controller.handle_mouse_position((29, 55))
        self.assertTrue(self.layout.nonogram.grid.is_cell_unknown(GridCoord(0, 0)))
