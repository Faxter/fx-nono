import sys
from pathlib import Path

from src.file_parser import parse
from src.nonogram import Nonogram
from src.ui.file_chooser import get_filepath_from_dialog
from src.ui.ui import Ui

CELL_SIZE = 25
FONT_SIZE = 20


def main(puzzle_path: Path):
    puzzle = parse(puzzle_path)
    nonogram = Nonogram(puzzle)
    ui = Ui(nonogram, CELL_SIZE, FONT_SIZE)
    ui.run()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        filepath = get_filepath_from_dialog("puzzles")
        if filepath.exists():
            main(filepath)
    else:
        main(Path(sys.argv[1]))
