from pathlib import Path
from typing import Tuple, List
import numpy as np


def get_stacks_procedures() -> Tuple[List[str], List[int]]:
    path = Path(__file__).parent / "input" / "input5.txt"

    with open(path, "r") as f:
        _stacks, _procedures = f.read().split("\n\n")

    _stacks = _stacks.splitlines()
    _stacks.pop()

    for row, values in enumerate(_stacks):
        _stacks[row] = [*values[1::4]]

    _stacks = np.array(_stacks).T.tolist()

    for row, values in enumerate(_stacks):
        _stacks[row] = [x for x in values if x != " "]
        _stacks[row].reverse()

    _procedures = _procedures.splitlines()

    for row, values in enumerate(_procedures):
        _procedures[row] = map(int, values.split(" ")[1::2])

    # _stacks = [["Z", "N"], ["M", "C", "D"], ["P"]]
    # _procedures = [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]

    return _stacks, _procedures


def part1(_stacks: list, _procedures: list) -> list:
    for _how_many, _from, _to in _procedures:
        for _ in range(_how_many):
            _stacks[_to - 1].append(_stacks[_from - 1].pop())
    return "".join(x[-1] for x in stacks)


def part2(_stacks: list, _procedures: list) -> list:
    for _how_many, _from, _to in _procedures:
        _stacks[_to - 1] = _stacks[_to - 1] + _stacks[_from - 1][-_how_many:]
        _stacks[_from - 1] = _stacks[_from - 1][:-_how_many]
    return "".join(x[-1] for x in stacks)


if __name__ == "__main__":
    stacks, procedures = get_stacks_procedures()
    print(part1(stacks, procedures))

    stacks, procedures = get_stacks_procedures()
    print(part2(stacks, procedures))
