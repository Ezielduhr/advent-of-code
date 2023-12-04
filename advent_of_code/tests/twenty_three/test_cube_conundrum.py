import pytest
from advent_of_code.twenty_three.cube_conundrum import CubeTool


@pytest.fixture()
def cube_input():
    cube_tool = CubeTool()
    challenge_input = """
Game 1: 10 green, 7 red, 6 blue; 12 green, 2 blue, 5 red; 7 green, 10 blue, 3 red; 11 green, 7 red; 5 blue, 8 green
Game 2: 1 green, 2 red; 2 blue, 1 green, 6 red; 5 red, 1 blue; 2 blue, 1 green, 1 red; 9 red
Game 3: 6 green, 4 blue, 1 red; 6 blue, 2 red, 1 green; 2 red, 5 blue, 4 green; 3 green, 6 blue, 1 red; 6 green, 12 blue, 1 red
Game 4: 2 blue, 4 red, 2 green; 6 red, 12 green, 4 blue; 1 blue, 6 red, 13 green
Game 5: 3 red, 1 blue; 2 red, 1 green, 2 blue; 3 blue, 2 red, 1 green; 1 red, 1 green, 1 blue
    """
    minimum_cubes = {"blue": 3, "red": 5, 'green': 2}

    yield cube_tool, challenge_input, minimum_cubes
    del cube_tool, challenge_input, minimum_cubes


def test_games_possible(cube_input):
    cube_tool, challenge_input, minimum_cubes = cube_input

    cube_tool.add_input(challenge_input)
    cube_tool.calculate_games_possible(minimum_cubes)

    assert cube_tool.games_possible[0] is True
    assert cube_tool.sum_of_game_possible == 8
