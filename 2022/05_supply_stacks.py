#!/usr/bin/env python3

from library import shared_functions
from copy import deepcopy as deep_copy


def parse_setup(setup_input):
    setup_input.reverse()
    first_line = True
    supply_stack = dict()

    for line in setup_input:
        cleaner_line = line.replace('\n', '')
        if first_line:
            first_line = False
            for number in cleaner_line:
                if number.isnumeric():
                    supply_stack[int(number)] = list()
            continue

        # Ho ho ho here starts the Christmas magic
        # To offset not starting with a space
        whitespace_counter = 1
        supply_stack_row = int()
        for char in cleaner_line:
            if char.isspace():
                whitespace_counter += 1
            if char.isalpha():
                whitespace_inbetween = (whitespace_counter-1)//4
                supply_stack_row += whitespace_inbetween+1
                supply_stack[supply_stack_row].append(char)
                whitespace_counter = 0
    return supply_stack


def parse_instructions(instructions_input):
    all_instructions = list()
    for line in instructions_input:
        all_instructions.append([element for element in line.split() if element.isdigit()])
    return all_instructions


def initialize_input():
    challenge_input = shared_functions.get_input("input_05.txt")

    end_of_setup = challenge_input.index('\n')
    raw_setup = challenge_input[:end_of_setup]
    raw_instructions = challenge_input[end_of_setup+1:]

    return parse_setup(raw_setup), parse_instructions(raw_instructions)


def main(starting_order, instructions_to_follow):
    # instructions to follow is a list in individual instructions where the
    # first element is the amount to move
    # second element is the stack to take it from
    # third element is the stack to place it
    # e.g. move 3 from 9 to 7

    # NOTE: Shallow copy just makes a new reference, deep copy makes an isolated duplicate
    actual_starting_order = deep_copy(starting_order)

    for instruction in instructions_to_follow:
        amount, source, destination = instruction
        # CrateMover9000
        for silly_iteration in range(int(amount)):
            crate = starting_order[int(source)].pop()
            starting_order[int(destination)].append(crate)

        # CrateMover9001
        for less_silly_iteration in reversed(range(int(amount))):
            index = (less_silly_iteration*-1)-1
            actual_crate = actual_starting_order[int(source)].pop(index)
            actual_starting_order[int(destination)].append(actual_crate)

    return starting_order, actual_starting_order


if __name__ == "__main__":
    start, instructions = initialize_input()
    final_state_supply_stack, actual_final_state_supply_stack = main(start, instructions)
    listy_list = list()
    actual_listy_list = list()
    for iteration in range(1, 10):
        listy_list.append(final_state_supply_stack[iteration][-1:][0])
        actual_listy_list.append(actual_final_state_supply_stack[iteration][-1:][0])

    print(f"top of supply stack after all instructions have been followed: {''.join(listy_list)}")
    print(f"top of supply stack after all instructions have been followed(9001): {''.join(actual_listy_list)}")
