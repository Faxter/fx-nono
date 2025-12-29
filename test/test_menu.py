import unittest
from unittest.mock import Mock

import src.menu


class TestMenu(unittest.TestCase):
    def test_menu_names(self):
        n = Mock()
        m = src.menu.Menu(n)
        self.assertListEqual(m.menu_names(), ["Open", "Save", "Load", "About"])

    def test_select_menu(self):
        src.menu.Menu.open = Mock()
        src.menu.Menu.save = Mock()
        src.menu.Menu.load = Mock()
        src.menu.Menu.about = Mock()
        n = Mock()
        m = src.menu.Menu(n)
        m.select_menu("Open")
        src.menu.Menu.open.assert_called_once()
        src.menu.Menu.save.assert_not_called()
        src.menu.Menu.load.assert_not_called()
        src.menu.Menu.about.assert_not_called()
