import json
from os.path import join
from pathlib import Path

import jsonpickle

from src.grid import Grid
from src.puzzle import Puzzle


def parse(filename: Path) -> Puzzle:
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return Puzzle(data["height"], data["width"], data["rows"], data["columns"])
    except FileNotFoundError:
        print(f"file {filename} could not be found")
        exit(1)
    except json.JSONDecodeError:
        print(f"could not decode JSON from {filename}")
        exit(1)


def write_savefile(filename: str, grid: Grid):
    filepath = join(Path.home(), "fx-nono", filename)
    try:
        with open(filepath, "w") as file:
            file.write(jsonpickle.encode(grid))
            print(f"game saved to {filepath}")
    except FileNotFoundError:
        print(f"file {filename} could not be found")
    except FileExistsError:
        print(f"file {filename} already exists")


def load_savefile(filename: str) -> Grid:
    filepath = join(Path.home(), "fx-nono", filename)
    try:
        with open(filepath, "r") as file:
            print(f"loading game state from {filepath}")
            grid = jsonpickle.decode(file.read())
            return grid
    except FileNotFoundError:
        print(f"file {filename} could not be found")
    except json.JSONDecodeError:
        print(f"could not decode JSON from {filename}")
    return Grid(0, 0)
