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
            single_game = {game_number: [
                {fixed_hand[1:].split(' ')[1]: int(fixed_hand[1:].split(' ')[0]) for fixed_hand in hand.split(',')} for hand
                in hands_from_bag]}

            self.games_played.update(single_game)

    def calculate_highest_per_game(self):
        for game_number, hands in self.games_played.items():
            temp_dict = {}
            for hand in hands:
                for colour, value in hand.items():
                    old_value = temp_dict.get(colour) or 0
                    if old_value < value:
                        temp_dict[colour] = value

            self.highest_numbers_per_game[game_number] = temp_dict

    def calculate_games_possible(self, challenge_input):
        for game, values in self.highest_numbers_per_game.items():
            if all([True if values[colour] <= value else False for colour, value in challenge_input.items()]):
                self.games_possible.append(int(game.split(' ')[1]))
        self.sum_of_games_possible = sum(self.games_possible)


def main(challenge_input, minimum_numbers):
    cube_tool = CubeTool()
    cube_tool.add_input(challenge_input)
    cube_tool.calculate_highest_per_game()
    cube_tool.calculate_games_possible(minimum_numbers)
    print("bla")


if __name__ == "__main__":
    minimum_numbers_input = {'red': 12, 'green': 13, 'blue': 14}
    main(GetInput('twenty_three').set_input("input_02.txt"), minimum_numbers_input)
