from src.cell_state import CellState
from src.grid import Grid
from src.hint import Hint
from src.puzzle import Puzzle


class Verifier:
    def __init__(self, puzzle: Puzzle, grid: Grid):
        self.puzzle = puzzle
        self.grid = grid

    def verify(self):
        for c in range(self.grid.columns):
            column = self.grid.get_column(c)
            if not self.verify_line(self.puzzle.column_hints[c], column):
                return False
        for r in range(self.grid.rows):
            row = self.grid.get_row(r)
            if not self.verify_line(self.puzzle.row_hints[r], row):
                return False
        return True

    def verify_line(self, hints: list[Hint], inputs: list[CellState]):
        i = 0
        counting = False
        current_length = 0
        block_lengths = []
        while i < len(inputs):
            if not counting:
                if inputs[i] == CellState.FULL:
                    counting = True
                    current_length = 1
                elif inputs[i] == CellState.EMPTY:
                    pass
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

        if len(hints) != len(block_lengths):
            return False

        for i in range(len(hints)):
            if hints[i].value != block_lengths[i]:
                return False
        return True
