from src.nonogram import Nonogram
from src.puzzle import Puzzle
from src.ui import Ui

PUZZLE_WIDTH = 5
PUZZLE_HEIGHT = 8
ROW_HINTS = [[3], [1, 1], [1, 1, 1], [1, 1, 1], [3], [3], [3], [1]]
COL_HINTS = [[3], [1, 3], [1, 6], [1, 3], [3]]
CELL_SIZE = 30


def main():
    puzzle = Puzzle(PUZZLE_HEIGHT, PUZZLE_WIDTH, ROW_HINTS, COL_HINTS)
    nonogram = Nonogram(puzzle)
    ui = Ui(nonogram, CELL_SIZE)
    ui.run()


if __name__ == "__main__":
    main()
