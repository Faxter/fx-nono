from src.nonogram import Nonogram
from src.puzzle import parse_puzzle
from src.ui import Ui

GRID_WIDTH = 5
GRID_HEIGHT = 10
CELL_SIZE = 50


def main():
    puzzle = parse_puzzle({"rows": GRID_HEIGHT, "columns": GRID_WIDTH})
    nonogram = Nonogram(puzzle)
    ui = Ui(nonogram, CELL_SIZE)
    ui.run()


if __name__ == "__main__":
    main()
