import pytest
from advent_of_code.twenty_three.cube_conundrum import CubeTool


@pytest.fixture()
def cube_input():
    cube_tool = CubeTool()
    # games possible 6 and 9
    test_input = """Game 5: 10 green, 7 red, 6 blue; 12 green, 2 blue, 5 red; 7 green, 10 blue, 3 red; 11 green, 7 red; 5 blue, 8 green
Game 6: 1 green, 2 red; 2 blue, 1 green, 6 red; 5 red, 1 blue; 2 blue, 1 green, 1 red; 9 red
Game 7: 6 green, 4 blue, 1 red; 6 blue, 2 red, 1 green; 2 red, 5 blue, 4 green; 3 green, 6 blue, 1 red; 6 green, 12 blue, 1 red
Game 8: 2 blue, 4 red, 2 green; 6 red, 12 green, 4 blue; 1 blue, 6 red, 13 green
Game 9: 3 red, 1 blue; 2 red, 1 green, 2 blue; 3 blue, 2 red, 1 green; 1 red, 1 green, 1 blue"""
    minimum_cubes = {"blue": 3, "red": 10, 'green': 6}

    yield cube_tool, test_input, minimum_cubes
    del cube_tool, test_input, minimum_cubes


def test_games_possible(cube_input):
    cube_tool, test_input, minimum_cubes = cube_input

    cube_tool.add_input(test_input)
    cube_tool.calculate_highest_per_game()
    cube_tool.calculate_games_possible(minimum_cubes)

    assert 6 in cube_tool.games_possible
    assert cube_tool.sum_of_games_possible == 15


def test_power_of_highest(cube_input):
    cube_tool, test_input, minimum_cubes = cube_input

    cube_tool.add_input(test_input)
    cube_tool.calculate_highest_per_game()
    cube_tool.calculate_power_of_highest()

    assert cube_tool.power_of_highest_numbers[0] == 840
    assert cube_tool.sum_of_power_highest_numbers == 1323
