import pytest
from advent_of_code.twenty_three.gear_ratios import GearTool


@pytest.fixture()
def gear_ratio_setup():
    gear_tool = GearTool()
    # TODO fix this horrible way of noting down test input
    test_input = """.362*366.................487+.48&.......600..180....845........................535...18...........397.#908....432*........229......346......
.................*................835....................578......*502...............*..416.............................................391.
....610&...514...501......./........*....*71.........../.......674......925...............*.869.....966........393................/.687.*...
............*...............786...248.104........92.633.....%..............*104...&466..138..@.........*.525...+......974......339..=...260.
....372/.889..............................55.406........134..250.=228..609...........................69...............*.....................
...........................................*........976...*...........=.......357...........................191.....150....................."""

    yield gear_tool, test_input
    del gear_tool, test_input


def test_sum_gear_successful(gear_ratio_setup):
    gear_tool, test_input = gear_ratio_setup
    gear_tool.read_grid(test_input)
    gear_tool.go_through_grid()
    gear_tool.calculate_sum_of_gears()
    assert gear_tool.sum_of_gears_counted == 18383
