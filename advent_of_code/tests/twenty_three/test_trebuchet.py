import pytest
from advent_of_code.twenty_three.trebuchet import CalibrationTool


@pytest.fixture()
def lines_to_calibrate():
    calibration_tester = CalibrationTool()
    test_input = """
eightqrssm9httwogqshfxninepnfrppfzhsc
one111jxlmc7tvklrmhdpsix
bptwone4sixzzppg
ninezfzseveneight5kjrjvtfjqt5nineone

5b32
1dtwone
six7two7sixtwo78
mvhsixpptztjh13sixthree2
six1bqqvrxndt
"""
    twone_input = "twone"
    yield calibration_tester, test_input, twone_input
    del calibration_tester, test_input, twone_input


def test_calibrate_success(lines_to_calibrate):
    calibration_tester, standard_test, _ = lines_to_calibrate
    calibration_tester.calibrate(standard_test)
    print("bla")


def test_all_lines_cover(lines_to_calibrate):
    pass


def test_overlapping_digits(lines_to_calibrate):
    calibration_tester, _, twone_input = lines_to_calibrate
    calibration_tester.calibrate(twone_input)

    assert calibration_tester.calibration_pairs[0] == int(21)

