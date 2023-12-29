import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from advent_of_code.settings import repo_root
from advent_of_code.twenty_three.trebuchet import CalibrationTool


feature_path = f"{repo_root}/advent_of_code/features/twenty_three/trebuchet.feature"


scenarios(feature_path)


@given(parsers.parse("calibration tool with the following input:\n{test_input}"), target_fixture='test_tool')
def setup_calibration_tool(test_input):
    # clean test input from TableData
    clean_input = test_input.replace('|', '')

    calibration_tool = CalibrationTool()
    calibration_tool.set_input(clean_input)

    yield calibration_tool
    del calibration_tool


@given("calibration tool is properly setup")
def check_calibration_tool(test_tool):
    if len(test_tool.stuff_to_calibrate_on) == 10:
        return True
    else:
        pytest.xfail("Calibration tool is not properly setup")


@when(parsers.parse("running trebuchet calibration tool for {line:d}"))
def run_calibration_tool(test_tool, line):
    test_tool.do_calibration(line)


@then(parsers.parse("the first digit found is {first_digit:d}"))
def check_first_digit(test_tool, first_digit):
    print(test_tool.temp_first_digit)
    print(test_tool.temp_last_digit)

    assert int(test_tool.temp_first_digit) == first_digit


@then(parsers.parse("the last digit found is {last_digit:d}"))
def check_last_digit(test_tool, last_digit):
    assert int(test_tool.temp_last_digit) == last_digit


@then(parsers.parse("adding these two together creates {number:d}"))
def check_concatenated_digits(test_tool, number):
    assert test_tool.calibration_pairs[0] == number


@when("summing all numbers together")
def sum_all_numbers(test_tool):
    test_tool.do_calibration()


@then(parsers.parse("the outcome should be {outcome:d}"))
def check_sum_of_numbers(test_tool, outcome):
    assert test_tool.calibration_sum == outcome


@given("calibration tool is set to improved version")
def set_calibration_tool_to_improved(test_tool):
    test_tool.set_improved_version()
