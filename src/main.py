import sys
from pathlib import Path

from src.file_parser import parse
from src.nonogram import Nonogram
from src.ui import Ui
from src.verifier import Verifier

CELL_SIZE = 30
FONT_SIZE = 25


def main():
    puzzle = parse(Path(sys.argv[1]))
    nonogram = Nonogram(puzzle)
    ui = Ui(nonogram, CELL_SIZE, FONT_SIZE)
    ui.run()
    verifier = Verifier(nonogram.puzzle, nonogram.grid)
    if verifier.verify():
        ui.display_success()
    else:
        ui.display_failure()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("no filepath to puzzle provided")
        exit(1)
    main()
