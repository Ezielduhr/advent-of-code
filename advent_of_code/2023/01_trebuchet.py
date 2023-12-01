from advent_of_code.utilities import GetInput


class CalibrationTool:
    def __init__(self):
        self.calibration_pairs = list()
        self.calibration_sum = int()

    def calibrate(self, stuff_to_calibrate_on: list):
        for line in stuff_to_calibrate_on.split("\n"):
            if line == '':
                continue
            # TODO fix "twone"
            improved_line = line.replace("one", "1").replace("two", "2").replace("three", "3").replace("four",
                                                                                                       "4").replace(
                "five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9")
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
    main(GetInput(2023).set_input("input_01.txt"))
