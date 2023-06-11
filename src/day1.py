from typing import List

import utils


def get_list_with_subtotals(list_with_blanks: List[str]) -> List[int]:

    out = []
    sub_total = 0
    for item in list_with_blanks:
        if item:
            sub_total += int(item)
        else:
            out.append(sub_total)
            sub_total = 0
    out.append(sub_total)

    return out


def part1(data: List[int]) -> int:
    return max(data)


def part2(data: List[int]) -> int:
    return sum(sorted(data, reverse=True)[:3])


if __name__ == "__main__":

    reindeer_food_items = utils.get_input("input1.txt")
    reindeer_calories = get_list_with_subtotals(reindeer_food_items)

    print(f"Day one part one: {part1(reindeer_calories):,}")
    print(f"Day one part two: {part2(reindeer_calories):,}")
