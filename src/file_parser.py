import json
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
    except IsADirectoryError:
        # this is raised when cancelling the dialog
        exit(1)


def write_savefile(filepath: Path, grid: Grid):
    try:
        with open(filepath, "w") as file:
            json = jsonpickle.encode(grid)
            if json:
                file.write(json)
                print(f"game saved to {filepath}")
            else:
                print("game state could not be encoded")
    except FileNotFoundError:
        print(f"file {filepath} could not be found")
    except FileExistsError:
        print(f"file {filepath} already exists")
    except IsADirectoryError:
        # this is raised when cancelling the dialog
        pass


def load_savefile(filepath: Path) -> Grid | None:
    try:
        with open(filepath, "r") as file:
            print(f"loading game state from {filepath}")
            grid = jsonpickle.decode(file.read())
            if type(grid) is Grid:
                return grid
            else:
                print(f"file {filepath} could not be decoded into correct type")
    except FileNotFoundError:
        print(f"file {filepath} could not be found")
    except json.JSONDecodeError:
        print(f"could not decode JSON from {filepath}")
    except IsADirectoryError:
        # this is raised when cancelling the dialog
        pass
