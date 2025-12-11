class Hint:
    def __init__(self, value: int):
        self.value = value
        self.crossed = False


def create_hints(hints: list[list[int]]) -> list[list[Hint]]:
    return [[Hint(value) for value in group] for group in hints]
