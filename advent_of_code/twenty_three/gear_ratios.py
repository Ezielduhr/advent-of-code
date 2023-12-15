import pandas
import itertools
import math
from advent_of_code.utilities import GetInput


class GearTool:
    def __init__(self):
        self.sum_of_gears_counted = int()
        self.df_grid = pandas.DataFrame
        self.numbers_with_symbols_adjacent = list()
        self.list_of_powers = list()
        self.sum_of_gears_counted = int()

    def calculate_sum_of_gears(self):
        self.sum_of_gears_counted = sum(self.numbers_with_symbols_adjacent)

    def read_grid(self, challenge_input):

        input_dict = {}
        for index, line in enumerate(challenge_input.split('\n')):
            input_dict[index] = [char for char in line]

        self.df_grid = pandas.DataFrame(input_dict)

    def check_adjacent_for_symbol(self, x_to_check, y_to_check):
        x_to_check = [x for x in (x_to_check-1, x_to_check, x_to_check+1)]
        y_to_check = [y for y in (y_to_check-1, y_to_check, y_to_check+1)]
        cords_to_check = list(itertools.chain.from_iterable([zip(x_to_check, [y, y, y]) for y in y_to_check]))
        for x, y in cords_to_check:
            if x == -1 or y == -1:
                continue
            try:
                char_to_check = self.df_grid.iloc[x, y]
                if not char_to_check.isalnum() and char_to_check != '.':
                    return True
            except IndexError:
                continue

    def find_number(self, _, start_x, start_y):
        number_buffer = list()
        char_to_check = self.df_grid.iloc[start_x, start_y]

        while char_to_check.isdigit():
            if start_x >= 0:
                start_x -= 1
                try:
                    char_to_check = self.df_grid.iloc[start_x, start_y]
                except IndexError:
                    break
            else:
                break

        start_x += 1
        char_to_check = self.df_grid.iloc[start_x, start_y]

        while char_to_check.isdigit():
            try:
                number_buffer.append(char_to_check)
                start_x += 1
                char_to_check = self.df_grid.iloc[start_x, start_y]
            except IndexError:
                break

        return int(''.join(number_buffer))

    def check_adjacent_for_two_numbers(self, x_to_check, y_to_check):
        x_to_check = [x for x in (x_to_check-1, x_to_check, x_to_check+1)]
        y_to_check = [y for y in (y_to_check-1, y_to_check, y_to_check+1)]

        cords_to_check = list(itertools.chain.from_iterable([zip(x_to_check, [y, y, y]) for y in y_to_check]))

        digits_found = list()
        for x, y in cords_to_check:
            if x == -1 or y == -1:
                continue
            try:
                char_to_check = self.df_grid.iloc[x, y]
                if char_to_check.isalnum():
                    digits_found.append((char_to_check, x, y))
            except IndexError:
                continue

        # Run through digits_found and remove adjacent numbers, so we don't count numbers twice
        previous_y = int()
        previous_x = int()
        to_remove = list()

        for digit, x, y in digits_found:
            if y == previous_y and x == previous_x+1:
                to_remove.append((digit, x, y))
            previous_x = x
            previous_y = y
        for thing in to_remove:
            digits_found.remove(thing)

        power = int()
        if len(digits_found) == 2:
            numbers_to_multiply = list()
            for digit in digits_found:
                numbers_to_multiply.append(self.find_number(*digit))
            power = math.prod(numbers_to_multiply)

        return power

    def go_through_grid(self):
        amount_of_rows, amount_of_column = self.df_grid.shape
        number_buffer = list()
        for current_y in range(0, amount_of_column):
            for current_x in range(0, amount_of_rows):
                current_char = self.df_grid.loc[current_x, current_y]

                if current_char.isdigit():
                    number_buffer.append([current_char, current_x, current_y])
                elif number_buffer and not current_char.isdigit():
                    checks_on_number = list()
                    actual_number = list()
                    for digit in number_buffer:
                        actual_number.append(digit[0])
                        checks_on_number.append(self.check_adjacent_for_symbol(digit[1], digit[2]))

                    if any(checks_on_number):
                        number_buffer = list()
                        self.numbers_with_symbols_adjacent.append(int(''.join(actual_number)))

                    else:
                        number_buffer = list()
                        checks_on_number = []
                        actual_number = []

                if current_char == "*":
                    power_of_adjacent_numbers = self.check_adjacent_for_two_numbers(current_x, current_y)
                    if power_of_adjacent_numbers:
                        self.list_of_powers.append(power_of_adjacent_numbers)

            if number_buffer:
                checks_on_number = list()
                actual_number = list()
                for digit in number_buffer:
                    actual_number.append(digit[0])
                    checks_on_number.append(self.check_adjacent_for_symbol(digit[1], digit[2]))

                if any(checks_on_number):
                    number_buffer = list()
                    self.numbers_with_symbols_adjacent.append(int(''.join(actual_number)))

                else:
                    number_buffer = list()
                    checks_on_number = []
                    actual_number = []


def main(challenge_input):
    gear_tool = GearTool()
    gear_tool.read_grid(challenge_input)
    gear_tool.go_through_grid()
    gear_tool.calculate_sum_of_gears()
    print(sum(gear_tool.numbers_with_symbols_adjacent))
    print(sum(gear_tool.list_of_powers))


if __name__ == "__main__":
    main(GetInput('twenty_three').set_input('input_03.txt'))
