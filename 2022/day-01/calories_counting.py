#!/usr/bin/env python3
from csv import reader as csv_reader
from git import Repo as git_repo
from os import path as os_path

repo_root = os_path.realpath(git_repo(__file__, search_parent_directories=True).working_tree_dir)
input_file = f"{repo_root}/2022/day-01/input_01.txt"


def main():
    with open(input_file, 'r') as input_stream:
        total_amount_per_elf = list()
        current_elf_food_amount = int()
        for line in input_stream.readlines():
            if line == '\n':
                total_amount_per_elf.append(current_elf_food_amount)
                current_elf_food_amount = int()
            else:
                current_elf_food_amount += int(line)

        print(f"Heaviest elf {max(total_amount_per_elf)}")
        print(f"Total calories of the three heaviest elfs {sum(sorted(total_amount_per_elf)[-3:])}")


if __name__ == "__main__":
    main()
