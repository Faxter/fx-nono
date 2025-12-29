import unittest
from unittest.mock import Mock, patch

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

    @patch("builtins.print")
    def test_open(self, mock_print):
        n = Mock()
        m = src.menu.Menu(n)
        m.open()
        mock_print.assert_called_once_with("open")

    @patch("src.menu.write_savefile")
    def test_save(self, mock_write):
        n = Mock()
        m = src.menu.Menu(n)
        m.save()
        mock_write.assert_called_once()

    @patch("src.menu.load_savefile")
    def test_load(self, mock_load):
        n = Mock()
        m = src.menu.Menu(n)
        m.load()
        mock_load.assert_called_once()
        n.set_grid.assert_called_once()

    @patch("builtins.print")
    def test_about(self, mock_print):
        n = Mock()
        m = src.menu.Menu(n)
        m.about()
        mock_print.assert_called_once_with("fx-nono")
