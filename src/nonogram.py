from src.cell_state import CellState
from src.grid import Grid
from src.hint import Hint
from src.puzzle import Puzzle


class Nonogram:
    def __init__(self, puzzle: Puzzle):
        self.puzzle = puzzle
        self.grid = Grid(puzzle.rows, puzzle.columns)

    def verify(self):
        for c in range(self.grid.columns):
            column = self.grid.get_column(c)
            if not verify_line(self.puzzle.column_hints[c], column):
                return False
        for r in range(self.grid.rows):
            row = self.grid.get_row(r)
            if not verify_line(self.puzzle.row_hints[r], row):
                return False
        return True

    def set_grid(self, grid: Grid):
        self.grid = grid


def verify_line(hints: list[Hint], inputs: list[CellState]):
    block_lengths = count_block_lengths(inputs)

    if len(hints) != len(block_lengths):
        return False

    for i in range(len(hints)):
        if hints[i].value != block_lengths[i]:
            return False
    return True


def count_block_lengths(inputs: list[CellState]):
    i = 0
    counting = False
    current_length = 0
    block_lengths: list[int] = []
    while i < len(inputs):
        if not counting:
            if inputs[i] == CellState.FULL:
                counting = True
                current_length = 1
        else:
            if inputs[i] == CellState.FULL:
                current_length += 1
            elif inputs[i] == CellState.EMPTY:
                counting = False
                block_lengths.append(current_length)
                current_length = 0
        i += 1
    if current_length > 0:
        block_lengths.append(current_length)
    return block_lengths
