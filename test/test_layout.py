import unittest

from src.nonogram import Nonogram
from src.puzzle import Puzzle
from src.ui.layout import Layout


class TestLayout(unittest.TestCase):
    def setUp(self):
        nonogram = Nonogram(Puzzle(3, 2, [[1], [1], [1]], [[1], [1]]))
        self.layout = Layout(nonogram)

    def test_create_layout(self):
        self.assertIsInstance(self.layout, Layout)

    def test_grid_coord_from_pos(self):
        coord = self.layout.grid_coord_from_position(2, 2)  # top right cell
        self.assertEqual(coord.column, 1)
        self.assertEqual(coord.row, 0)

    def test_is_on_grid(self):
        self.assertTrue(self.layout.is_on_grid(2, 2))  # top right
        self.assertTrue(self.layout.is_on_grid(1, 2))  # top left
        self.assertTrue(self.layout.is_on_grid(2, 3))  # bot right
        self.assertTrue(self.layout.is_on_grid(1, 3))  # bot left

        self.assertFalse(self.layout.is_on_grid(0, 0))
        self.assertFalse(self.layout.is_on_grid(1, 0))
        self.assertFalse(self.layout.is_on_grid(0, 1))
        self.assertFalse(self.layout.is_on_grid(2, 1))
        self.assertFalse(self.layout.is_on_grid(1, 5))
        self.assertFalse(self.layout.is_on_grid(3, 1))

    def test_is_on_top_hint(self):
        self.assertTrue(self.layout.is_on_top_hint(1, 1))
        self.assertTrue(self.layout.is_on_top_hint(2, 1))

        self.assertFalse(self.layout.is_on_top_hint(0, 0))
        self.assertFalse(self.layout.is_on_top_hint(2, 2))
        self.assertFalse(self.layout.is_on_top_hint(0, 1))

    def test_is_on_left_hint(self):
        self.assertTrue(self.layout.is_on_left_hint(0, 2))
        self.assertTrue(self.layout.is_on_left_hint(0, 4))

        self.assertFalse(self.layout.is_on_left_hint(0, 0))
        self.assertFalse(self.layout.is_on_left_hint(1, 0))
        self.assertFalse(self.layout.is_on_left_hint(2, 2))
