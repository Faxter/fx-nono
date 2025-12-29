import unittest
from unittest.mock import Mock

import src.menu


class TestMenu(unittest.TestCase):
    def test_menu_names(self):
        m = src.menu.Menu()
        self.assertListEqual(m.menu_names(), ["Open", "Save", "Load", "About"])

    def test_select_menu(self):
        src.menu.open = Mock()
        src.menu.save = Mock()
        src.menu.load = Mock()
        src.menu.about = Mock()
        m = src.menu.Menu()
        m.select_menu("Open")
        src.menu.open.assert_called_once()
        src.menu.save.assert_not_called()
        src.menu.load.assert_not_called()
        src.menu.about.assert_not_called()
