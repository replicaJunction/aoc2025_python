"""Supporting logic to work with a "safe." See Day 1."""

import re
from dataclasses import dataclass
from typing import Literal


@dataclass
class Rotation:
    """Single rotation instruction for a safe."""

    direction: Literal["L"] | Literal["R"]
    amount: int


_ROTATION_REGEX = re.compile(r"^\s*(?P<dir>[L|R])(?P<count>\d+)\s*$")
_SAFE_MIN_DIGIT = 0
_SAFE_MAX_DIGIT = 99
_SAFE_DIGIT_COUNT = _SAFE_MAX_DIGIT - _SAFE_MIN_DIGIT + 1


def _rotate_left(position: int, amount: int) -> tuple[int, int]:
    # zero_count = abs(position - amount) // _SAFE_DIGIT_COUNT
    zero_count = 0
    if position <= _SAFE_MIN_DIGIT:
        new_position = position + _SAFE_DIGIT_COUNT - amount
    else:
        new_position = position - amount
    while new_position < _SAFE_MIN_DIGIT:
        new_position += _SAFE_DIGIT_COUNT
        zero_count += 1
    if new_position == 0:
        zero_count += 1
    return (new_position, zero_count)


def _rotate_right(position: int, amount: int) -> tuple[int, int]:
    # zero_count = (position + amount) // _SAFE_DIGIT_COUNT
    new_position = position + amount
    zero_count = 0
    while new_position > _SAFE_MAX_DIGIT:
        new_position -= _SAFE_DIGIT_COUNT
        zero_count += 1
    return (new_position, zero_count)


def rotate_dial(position: int, rotation: Rotation) -> tuple[int, int]:
    """Rotate the dial according to the given instruction.

    Args:
        position: Current position of the dial

        rotation: Rotation instruction to follow for the dial

    Returns:
        The new position of the dial after performing the rotation.
    """
    match rotation.direction:
        case "L":
            return _rotate_left(position, rotation.amount)
        case "R":
            return _rotate_right(position, rotation.amount)
        case _:
            raise ValueError("Unhandled rotation value")


def parse_rotation_from_line(text: str) -> Rotation:
    """Parse a `Rotation` from a line of text."""
    matches = _ROTATION_REGEX.match(text)
    if not matches:
        raise ValueError("Could not parse a rotation from the given text")
    groups = matches.groupdict()
    dir = str(groups.get("dir"))
    if dir not in ("L", "R"):
        raise ValueError("Invalid direction: expected L or R, got " + dir)
    count_text = str(groups.get("count"))
    try:
        count = int(count_text)
    except ValueError as exn:
        raise ValueError("Invalid count: expected a valid integer") from exn
    return Rotation(direction=dir, amount=count)
