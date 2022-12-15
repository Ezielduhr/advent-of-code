#!/usr/bin/env python3

from library import shared_functions


def sections_overlap(start_first, end_first, start_second, end_second, strict):
    if strict:
        if (start_first >= start_second and end_first <= end_second) or \
                (start_second >= start_first and end_second <= end_first):
            return True
    else:
        first = set(range(start_first, end_first+1))
        second = set(range(start_second, end_second+1))

        if first.intersection(second) or \
                second.intersection(first):
            return True


def main():
    challenge_input = shared_functions.get_input("input_04.txt")
    obvious_assignment_screw_ups = int()
    just_screw_ups = int()

    for line in challenge_input:
        sections = line.replace('\n', '').split(',')
        first_section = sections[0]
        second_section = sections[1]

        start_first_section = int(first_section.split('-')[0])
        end_first_section = int(first_section.split('-')[1])
        start_second_section = int(second_section.split('-')[0])
        end_second_section = int(second_section.split('-')[1])
        # NOTE: if you're using str for the comparison 7 is somehow greater or equal than 16

        if sections_overlap(start_first_section, end_first_section, start_second_section, end_second_section, True):
            obvious_assignment_screw_ups += 1

        if sections_overlap(start_first_section, end_first_section, start_second_section, end_second_section, False):
            just_screw_ups += 1

    return obvious_assignment_screw_ups, just_screw_ups


if __name__ == "__main__":
    obvious, just = main()
    print(f"times on section is entirely cleaned by paired elf: {obvious}")
    print(f"Just general silliness {just}")
