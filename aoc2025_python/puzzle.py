from collections.abc import Iterable
from pathlib import Path


def read_puzzle_input(base_name: str) -> Iterable[str]:
    """Read the puzzle input for the given day."""
    filename = base_name + ".txt"
    current_file_path = Path(__file__)
    input_file = current_file_path.parent.parent / "inputs" / filename
    with input_file.open(mode="r", encoding="UTF-8") as file:
        for line in file:
            yield line.strip()
