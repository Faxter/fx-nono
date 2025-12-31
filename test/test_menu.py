import unittest
from unittest.mock import Mock, patch

import src.menu


class TestMenu(unittest.TestCase):
    def test_menu_names(self):
        n = Mock()
        m = src.menu.Menu(n)
        self.assertListEqual(m.menu_names(), ["Save", "Load", "About"])

    def test_select_menu(self):
        src.menu.Menu.save = Mock()
        src.menu.Menu.load = Mock()
        src.menu.Menu.about = Mock()
        n = Mock()
        m = src.menu.Menu(n)
        m.select_menu("Save")
        src.menu.Menu.save.assert_called_once()
        src.menu.Menu.load.assert_not_called()
        src.menu.Menu.about.assert_not_called()

    @patch("src.menu.get_filepath_to_save_as_from_dialog")
    @patch("src.menu.write_savefile")
    def test_save(self, mock_write, mock_dialog):
        n = Mock()
        m = src.menu.Menu(n)
        m.save()
        mock_write.assert_called_once()

    @patch("src.menu.get_filepath_from_dialog")
    @patch("src.menu.load_savefile")
    def test_load(self, mock_load, mock_dialog):
        # mock_dialog.return_value
        n = Mock()
        m = src.menu.Menu(n)
        m.load()
        mock_dialog.assert_called_once()
        mock_load.assert_called_once()
        n.set_grid.assert_called_once()

    @patch("src.menu.get_filepath_from_dialog")
    @patch("src.menu.load_savefile")
    def test_load_invalid_grid(self, mock_load, mock_dialog):
        n = Mock()
        m = src.menu.Menu(n)
        mock_load.return_value = None
        m.load()
        mock_dialog.assert_called_once()
        mock_load.assert_called_once()
        n.set_grid.assert_not_called()

    @patch("builtins.print")
    @patch("src.menu.get_filepath_from_dialog")
    @patch("src.menu.load_savefile")
    def test_load_malformed_grid(self, mock_load, mock_dialog, mock_print):
        n = Mock()
        n.is_compatible.return_value = False
        m = src.menu.Menu(n)
        m.load()
        mock_dialog.assert_called_once()
        mock_load.assert_called_once()
        n.set_grid.assert_not_called()
        mock_print.assert_called_once()

    @patch("src.menu.show_message")
    def test_about(self, mock_msg_box):
        n = Mock()
        m = src.menu.Menu(n)
        m.about()
        mock_msg_box.assert_called_once()
