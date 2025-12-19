"""Unit tests for the `rotate_dial` function."""

import pytest

from aoc2025_python.safe import Rotation, rotate_dial


@pytest.mark.parametrize(
    "position,rotation,expected",
    (
        (50, Rotation("L", 68), (82, 1)),
        (82, Rotation("L", 30), (52, 0)),
        (52, Rotation("R", 48), (0, 1)),
        (0, Rotation("L", 5), (95, 0)),
        (95, Rotation("R", 60), (55, 1)),
        (55, Rotation("L", 55), (0, 1)),
        (0, Rotation("L", 1), (99, 0)),
        (99, Rotation("L", 99), (0, 1)),
        (0, Rotation("R", 14), (14, 0)),
        (14, Rotation("L", 82), (32, 1)),
        (50, Rotation("R", 1000), (50, 10)),
    ),
)
def test_examples(position: int, rotation: Rotation, expected: tuple[int, int]) -> None:
    """Test examples provided from the AoC documentation."""
    actual_value = rotate_dial(position, rotation)
    assert expected == actual_value
