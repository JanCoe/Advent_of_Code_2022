import unittest

import day1
from day2 import Player, extract_choices_part1, extract_choices_part2
import day3
from day3 import split_items, get_set

TEST_DAY1 = [
    "1000",
    "2000",
    "3000",
    "",
    "4000",
    "",
    "5000",
    "6000",
    "",
    "7000",
    "8000",
    "9000",
    "",
    "10000",
]


class TestDayOne(unittest.TestCase):
    def test_day1(self):
        reindeer_calories = day1.get_list_with_subtotals(TEST_DAY1)

        part1 = day1.part1(reindeer_calories)
        part2 = day1.part2(reindeer_calories)

        self.assertEqual(part1, 24_000)
        self.assertEqual(part2, 45_000)


STRATEGIES = ["A Y", "B X", "C Z"]


class TestDayTwo(unittest.TestCase):

    def test_day2_part1(self):
        player2_scores = [8, 1, 6]

        player1 = Player("")
        player2 = Player("")

        for choices, score in zip(STRATEGIES, player2_scores):
            player1.choice, player2.choice = extract_choices_part1(choices)

            self.assertEqual(player2.update_points(player1), score)

        self.assertEqual(player2.score, sum(player2_scores))

    def test_day2_part2(self):
        player2_scores = [4, 1, 7]

        player1 = Player("")
        player2 = Player("")

        for choices, score in zip(STRATEGIES, player2_scores):
            player1.choice, player2.choice = extract_choices_part2(choices)

            self.assertEqual(player2.update_points(player1), score)

        self.assertEqual(player2.score, sum(player2_scores))


RUCKSACKS_TEST = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]


class TestDayThree(unittest.TestCase):

    def test_day3_part1(self):

        results = [16, 38, 42, 22, 20, 19]
        ctr = 0
        for rucksack in RUCKSACKS_TEST:
            items_1, items_2 = split_items(rucksack)

            items_1 = get_set(items_1)
            items_2 = get_set(items_2)

            self.assertEqual(items_1.intersection(items_2), {results[ctr]})
            ctr += 1

    def test_day3_part1(self):

        self.assertEqual(day3.part2(RUCKSACKS_TEST), 70)


if __name__ == '__main__':
    unittest.main()
