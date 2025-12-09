from src.grid import Grid
from src.puzzle import Puzzle


class Nonogram:
    def __init__(self, puzzle: Puzzle):
        self.puzzle = puzzle
        self.grid = Grid(puzzle.rows, puzzle.columns)
