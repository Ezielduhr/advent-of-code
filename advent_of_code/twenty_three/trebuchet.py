from advent_of_code.utilities import GetInput


class CalibrationTool:
    def __init__(self):
        self.stuff_to_calibrate_on = str()
        self.calibration_pairs = list()
        self.calibration_sum = int()
        self.temp_first_digit = int()
        self.temp_last_digit = int()
        self.improved_version = False

    def set_input(self, stuff_to_calibrate_on: str):
        # Had I known BDD before writing this I would have done this better
        self.stuff_to_calibrate_on = stuff_to_calibrate_on.split("\n")

    def set_improved_version(self):
        self.improved_version = True

    def _calibrate(self, line_to_calibrate):
        line = line_to_calibrate.replace(" ", '')
        if not line:
            return False

        if self.improved_version:
            # dirty fix for the 'twone' overlapping replace problem
            line = line_to_calibrate.replace("one", "one1one").replace("two", "two2two").replace("three",
                                                                                                 "three3three").replace(
                "four",
                "four4four").replace(
                "five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight",
                                                                                                       "eight8eight").replace(
                "nine", "nine9nine")

        all_integers = [char for char in line if char.isnumeric()]

        self.temp_first_digit = all_integers[0]
        self.temp_last_digit = all_integers[-1]
        self.calibration_pairs.append(int(f"{self.temp_first_digit}{self.temp_last_digit}"))

    def do_calibration(self, lines_index=None):
        if lines_index:
            self._calibrate(self.stuff_to_calibrate_on[lines_index-1])
        else:
            for line in self.stuff_to_calibrate_on:
                self._calibrate(line)

        self.calibration_sum = sum(self.calibration_pairs)


def main(challenge_input):
    calibration = CalibrationTool()
    calibration.do_calibration(challenge_input)
    print(calibration.calibration_sum)


if __name__ == "__main__":
    main(GetInput("twenty_three").set_input("input_01.txt"))
