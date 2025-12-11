import unittest

from src.hint import Hint, create_hints


class TestHint(unittest.TestCase):
    def test_create_hint(self):
        h = Hint(1)
        self.assertIsInstance(h, Hint)
        self.assertEqual(h.value, 1)
        self.assertEqual(h.crossed, False)

    def test_create_hint_list_from_int_list(self):
        hints = create_hints([[1], [3, 3]])
        self.assertEqual(hints[0][0].value, 1)
        self.assertEqual(hints[1][0].value, 3)
        self.assertEqual(hints[1][1].value, 3)

    def test_toggle_crossed(self):
        hint = Hint(1)
        hint.toggle_crossed()
        self.assertTrue(hint.crossed)
