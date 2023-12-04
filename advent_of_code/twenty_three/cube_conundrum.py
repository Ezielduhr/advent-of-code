from advent_of_code.utilities import GetInput


class CubeTool:
    def __init__(self):
        self.games_played = dict()
        self.highest_numbers_per_game = dict()
        self.games_possible = list()
        self.sum_of_games_possible = int()

    def add_input(self, challenge_input):
        for line in challenge_input.split('\n'):
            game_number, games = line.split(':')
            hands_from_bag = games.split(';')
            single_game = {game_number: [{fixed_hand[1:].split(' ')[1]: fixed_hand[1:].split(' ')[0] for fixed_hand in hand.split(',')} for hand in hands_from_bag]}

            self.games_played.update(single_game)


    def calculate_games_possible(self, challenge_input):
        pass


def main(challenge_input, minimum_numbers):
    cube_tool = CubeTool()
    cube_tool.add_input(challenge_input)
    cube_tool.calculate_games_possible(minimum_numbers)


if __name__ == "__main__":
    minimum_numbers_input = {'red': 12, 'green': 13, 'blue': 14}
    main(GetInput('twenty_three').set_input("input_02.txt"), minimum_numbers_input)
