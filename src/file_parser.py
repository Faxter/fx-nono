import json
from pathlib import Path

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


def write_savefile(filename: Path, grid: Grid):
    try:
        with open(filename, "w") as file:
            json.dump(grid, file)
    except FileNotFoundError:
        print(f"file {filename} could not be found")
    except FileExistsError:
        print(f"file {filename} already exists")


def load_savefile(filename: Path) -> Grid:
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"file {filename} could not be found")
    except json.JSONDecodeError:
        print(f"could not decode JSON from {filename}")
    return Grid(0, 0)
