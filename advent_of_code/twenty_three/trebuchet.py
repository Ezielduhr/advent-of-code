from advent_of_code.utilities import GetInput


class CalibrationTool:
    def __init__(self):
        self.calibration_pairs = list()
        self.calibration_sum = int()

    def calibrate(self, stuff_to_calibrate_on: str):
        for line in stuff_to_calibrate_on.split("\n"):
            if line == '':
                continue
            # dirty fix for the 'twone' overlapping replace problem
            improved_line = line.replace("one", "one1one").replace("two", "two2two").replace("three",
                                                                                             "three3three").replace(
                "four",
                "four4four").replace(
                "five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight",
                                                                                                       "eight8eight").replace(
                "nine", "nine9nine")
            all_integers = [char for char in improved_line if char.isnumeric()]
            first_int = all_integers[0]
            last_int = all_integers[-1]
            self.calibration_pairs.append(int(f"{first_int}{last_int}"))
        self.calibration_sum = sum(self.calibration_pairs)


def main(challenge_input):
    calibration = CalibrationTool()
    calibration.calibrate(challenge_input)
    print(calibration.calibration_sum)


if __name__ == "__main__":
    main(GetInput("twenty_three").set_input("input_01.txt"))
