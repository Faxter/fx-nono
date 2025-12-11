import json
from pathlib import Path

from src.puzzle import Puzzle


def parse(filename: Path):
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
