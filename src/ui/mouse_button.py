from enum import Enum


class MouseButton(Enum):
    LEFT = 1
    MIDDLE = 2
    RIGHT = 3


def get_mouse_button(index: int) -> MouseButton:
    match index:
        case 1:
            return MouseButton.LEFT
        case 2:
            return MouseButton.MIDDLE
        case 3:
            return MouseButton.RIGHT
        case _:
            return MouseButton.LEFT
