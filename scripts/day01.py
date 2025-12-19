import re

from aoc2025_python.puzzle import read_puzzle_input
from aoc2025_python.safe import parse_rotation_from_line, rotate_dial

_ROTATION_REGEX = re.compile(r"^\s*(?P<dir>[L|R])(?P<count>\d+)\s*$")
_SAFE_MIN_DIGIT = 0
_SAFE_MAX_DIGIT = 99
_SAFE_DIGIT_COUNT = _SAFE_MAX_DIGIT - _SAFE_MIN_DIGIT + 1


def part1() -> None:
    """Count the number of times the dial lands on zero."""
    puzzle_input = read_puzzle_input("day01")
    safe_value = 50
    zero_count = 0
    for line in puzzle_input:
        rotation = parse_rotation_from_line(line)
        new_value, _ = rotate_dial(safe_value, rotation)
        if new_value == 0:
            zero_count += 1
            print(f"{line}\t{safe_value}->{new_value} (!)")
        else:
            print(f"{line}\t{safe_value}->{new_value}")

        safe_value = new_value

    print()
    print(f"Final safe value: {safe_value}")
    print(f"Total zeroes: {zero_count}")


def part2() -> None:
    """Count the number of times any click points to zero mid-rotation."""
    puzzle_input = read_puzzle_input("day01")
    safe_value = 50
    zero_count = 0
    for line in puzzle_input:
        rotation = parse_rotation_from_line(line)
        new_value, new_zero_count = rotate_dial(safe_value, rotation)
        log_line = f"{line}\t{safe_value}->{new_value}"
        if new_zero_count > 0:
            zero_count += new_zero_count
            log_line += f" ({new_zero_count}, {zero_count})"
        print(log_line)

        safe_value = new_value

    print()
    print(f"Final safe value: {safe_value}")
    print(f"Total zeroes: {zero_count}")


def main() -> None:
    part2()


if __name__ == "__main__":
    main()
