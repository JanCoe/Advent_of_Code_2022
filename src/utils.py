from pathlib import Path


def get_input(file_name: str) -> list:
    path = Path(__file__).parent / "input" / file_name

    with open(path, "r") as f:
        out = f.read().splitlines()

    return out
