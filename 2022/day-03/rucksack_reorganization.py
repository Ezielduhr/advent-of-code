#!/usr/bin/env python3

from git import Repo as git_Repo
from os import path as os_path
from string import ascii_lowercase as string_ascii_lowercase, ascii_uppercase as string_ascii_uppercase

repo_root = os_path.realpath(git_Repo(__file__, search_parent_directories=True).working_tree_dir)
input_file = f"{repo_root}/2022/day-03/input_03.txt"
priority_translation = dict()
rucksack_content = list()


def initialize_globals():
    global priority_translation
    x = 1

    for lowercase in string_ascii_lowercase:
        priority_translation[lowercase] = x
        x += 1

    for uppercase in string_ascii_uppercase:
        priority_translation[uppercase] = x
        x += 1

    global rucksack_content
    with open(input_file, 'r') as input_stream:
        rucksack_content = [line.replace('\n', '') for line in input_stream.readlines()]


def get_total_priority():
    # assumption: the duplicated item is never the first item in the second rucksack
    duplicated_items = list()
    for line in rucksack_content:
        half_but_not_really = int(len(line)/2)
        first_rucksack = line[:half_but_not_really]
        second_rucksack = line[half_but_not_really:]

        duplicated_items.append(set(first_rucksack).intersection(set(second_rucksack)))

    total_priority = int()
    for item in duplicated_items:
        letter = ''.join(item)
        total_priority += priority_translation[letter]
    return total_priority


def get_security_badges():
    # Create logical elf groups and find their badge
    elf_groups = zip(*[iter(rucksack_content)] * 3)
    badges = list()
    for group in elf_groups:
        contents_set = [set(elf) for elf in group]
        false_security_badge = set.intersection(*map(set, contents_set))
        badges.append(false_security_badge)

    badge_priority = int()
    for badge in badges:
        clean_badge = ''.join(badge)
        badge_priority += priority_translation[clean_badge]

    return badge_priority


def main():
    initialize_globals()
    return get_total_priority(), get_security_badges()


if __name__ == '__main__':
    print(main())
