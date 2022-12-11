#!/usr/bin/env python3
from typing import Dict
from git import Repo as git_Repo
from os import path as os_path

repo_root = os_path.realpath(git_Repo(__file__, search_parent_directories=True).working_tree_dir)
input_file = f"{repo_root}/2022/day-02/input_02.txt"


def main(point_system):
    total_score: int = int()
    with open(input_file, newline='') as input_stream:
        for line in input_stream.readlines():
            rps_scenario = line.replace(' ', '').replace('\n', '')
            total_score += point_system[rps_scenario]

    return total_score


if __name__ == "__main__":
    # A = Rock(1), B = Paper(2), C = Scissor(3)
    # X = lose(0), Y = draw(3), Z = win(6)
    # rps = rock paper scissor

    secret_strategy_possible_scores: dict[str, int] = dict(AX=4, BX=1, CX=7, AY=8, BY=5, CY=2, AZ=3, BZ=9, CZ=6)
    actual_secret_strategy_possible_scores: dict[str, int] = dict(AX=3, BX=1, CX=2, AY=4, BY=5, CY=6, AZ=8, BZ=9, CZ=7)

    print(main(secret_strategy_possible_scores))
    print(main(actual_secret_strategy_possible_scores))
