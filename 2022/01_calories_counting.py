#!/usr/bin/env python3
from library import shared_functions


def main():
    challenge_input = shared_functions.get_input("input_01.txt")

    total_amount_per_elf = list()
    current_elf_food_amount = int()
    for line in challenge_input:
        # NOTE: last elf isn't counted
        if line == '\n':
            total_amount_per_elf.append(current_elf_food_amount)
            current_elf_food_amount = int()
        else:
            current_elf_food_amount += int(line)

    return total_amount_per_elf


if __name__ == "__main__":
    print(f"Heaviest elf weighs: {max(main())}")
    print(f"Total calories of the three heaviest elfs: {sum(sorted(main())[-3:])}")
