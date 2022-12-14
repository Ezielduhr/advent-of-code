#!/usr/bin/env python3
from typing import Dict
from library import shared_functions


def main(point_system):
    challenge_input = shared_functions.get_input("input_02.txt")

    total_score: int = int()
    for line in challenge_input:
        rps_scenario = line.replace(' ', '').replace('\n', '')
        total_score += point_system[rps_scenario]

    return total_score


if __name__ == "__main__":
    # A = Rock(1), B = Paper(2), C = Scissor(3)
    # X = lose(0), Y = draw(3), Z = win(6)
    # rps = rock paper scissor

    secret_strategy_possible_scores: dict[str, int] = dict(AX=4, BX=1, CX=7, AY=8, BY=5, CY=2, AZ=3, BZ=9, CZ=6)
    actual_secret_strategy_possible_scores: dict[str, int] = dict(AX=3, BX=1, CX=2, AY=4, BY=5, CY=6, AZ=8, BZ=9, CZ=7)

    print(f"total score using secret strategy: {main(secret_strategy_possible_scores)}")
    print(f"total score using actual secret strategy: {main(actual_secret_strategy_possible_scores)}")
