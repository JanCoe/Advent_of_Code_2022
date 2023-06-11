import utils


def range_contained(line_of_data: str) -> bool:
    first, second = line_of_data.split(",")
    first_min, first_max = map(int, first.split("-"))
    second_min, second_max = map(int, second.split("-"))

    return ((first_min >= second_min) and (first_max <= second_max)) or (
        (second_min >= first_min) and (second_max <= first_max)
    )


def range_overlaps(line_of_data: str) -> bool:
    first, second = line_of_data.split(",")
    first_min, first_max = map(int, first.split("-"))
    second_min, second_max = map(int, second.split("-"))

    return not ((first_max < second_min) or (second_max < first_min))


def part1(my_data: list):
    number_ranges_contained = sum([range_contained(line) for line in my_data])
    print(f"Part 1 answer is {number_ranges_contained}.")


def part2(my_data: list):
    number_ranges_overlap = sum([range_overlaps(line) for line in my_data])
    print(f"Part 2 answer is {number_ranges_overlap}.")


if __name__ == "__main__":
    # data = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]

    data = utils.get_input("input4.txt")

    part1(data)
    part2(data)
