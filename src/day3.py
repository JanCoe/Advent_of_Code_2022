from typing import Tuple, List

import utils


def split_items(items: str) -> Tuple[str, str]:
    num_items = len(items) // 2
    return items[:num_items], items[num_items:]


def get_priority(x: str) -> int:
    if "a" <= x <= "z":
        return ord(x) - ord("a") + 1
    elif "A" <= x <= "Z":
        return ord(x) - ord("A") + 27
    else:
        raise RuntimeError(f"Value of {x} not in range.")


def get_set(items: str) -> set:
    return {get_priority(item) for item in items}


def part1(rucksacks: List[str]):
    result = 0
    for rucksack in rucksacks:
        items_1, items_2 = split_items(rucksack)
        result += sum(get_set(items_1).intersection(get_set(items_2)))

    print(f"Sum of the priorities is {result}.")


def part2(rucksacks: List[str]) -> int:

    groups = len(rucksacks) // 3

    rucksack_ctr = 0
    result = 0
    for ctr in range(groups):

        items_1 = rucksacks[rucksack_ctr + 0]
        items_2 = rucksacks[rucksack_ctr + 1]
        items_3 = rucksacks[rucksack_ctr + 2]

        rucksack_ctr += 3
        result += sum(get_set(items_1).intersection(get_set(items_2), get_set(items_3)))

    print(f"Sum of the priorities is {result}.")

    return result


if __name__ == "__main__":
    rucksacks_data = utils.get_input("input3.txt")

    part1(rucksacks_data)
    part2(rucksacks_data)
