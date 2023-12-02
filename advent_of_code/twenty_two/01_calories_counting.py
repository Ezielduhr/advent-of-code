#!/usr/bin/env python3
from library.shared_functions import get_input


def main():
    """ Creates a list of total calories per elf """
    challenge_input = get_input("input_01.txt")

    total_amount_per_elf = list()
    current_elf_food_amount = int()
    for line in challenge_input:
        if line == '\n':
            total_amount_per_elf.append(current_elf_food_amount)
            current_elf_food_amount = int()
        else:
            current_elf_food_amount += int(line)

    if current_elf_food_amount:
        # This statement makes sure that the last elf is counted
        # even if there's no new line at the end of the input file
        total_amount_per_elf.append(current_elf_food_amount)
    return total_amount_per_elf


if __name__ == "__main__":
    print(f"Heaviest elf weighs: {max(main())}")
    print(f"Total calories of the three heaviest elfs: {sum(sorted(main())[-3:])}")
