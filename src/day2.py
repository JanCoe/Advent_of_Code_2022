from __future__ import annotations
from typing import Tuple, Callable

import utils

MAPPING = {"A": "R", "B": "P", "C": "S"}


class Player:

    choice: str
    score: int = 0

    def __init__(self, choice: str):
        self.choice = choice

    def __gt__(self, other: Player) -> bool:

        if (self.choice, other.choice) in [("R", "S"), ("S", "P"), ("P", "R")]:
            return True
        else:
            return False

    def __eq__(self, other: Player) -> bool:
        return self.choice == other.choice

    def update_points(self, other: Player) -> int:
        score_outcome = (self > other) * 6 + (self == other) * 3
        score_choice = (
            (self.choice == "R") + (self.choice == "P") * 2 + (self.choice == "S") * 3
        )
        score_round = score_outcome + score_choice

        self.score += score_round

        return score_round


def extract_choices_part1(item: str) -> Tuple[str, str]:
    choice_1, choice_2 = item.split(" ")
    mapping_2 = {"X": "R", "Y": "P", "Z": "S"}
    return MAPPING[choice_1], mapping_2[choice_2]


def extract_choices_part2(item: str) -> Tuple[str, str]:
    choice_1, choice_2 = item.split(" ")

    choice_1 = MAPPING[choice_1]

    player1 = Player(choice_1)

    valid_choices = {"R", "P", "S"}
    valid_choices.remove(choice_1)

    if choice_2 == "Y":  # draw
        choice_2 = choice_1
    elif choice_2 == "X":  # loose for player2
        for ctr in valid_choices:
            player2 = Player(ctr)
            if player2 < player1:
                choice_2 = ctr
                break
    else:  # win for player2
        for ctr in valid_choices:
            player2 = Player(ctr)
            if player2 > player1:
                choice_2 = ctr
                break

    return choice_1, choice_2


def calculate_scores(extract_choices: Callable) -> None:
    player1 = Player("")
    player2 = Player("")

    data = utils.get_input("input2.txt")

    for item in data:
        player1.choice, player2.choice = extract_choices(item)

        player1.update_points(player2)
        player2.update_points(player1)

    print(f"{player1.score = :,}, {player2.score = :,}")


if __name__ == "__main__":
    calculate_scores(extract_choices_part1)
    calculate_scores(extract_choices_part2)
