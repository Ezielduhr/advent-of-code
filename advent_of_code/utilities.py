from advent_of_code.settings import repo_root


class GetInput:
    def __init__(self, year):
        self.year = year
        self.input = None

    def set_input(self, file_name, path_to_file=None):
        if path_to_file:
            input_file = f"{repo_root}/advent_of_code/{path_to_file}/{file_name}"
        else:
            input_file = f"{repo_root}/advent_of_code/{self.year}/library/{file_name}"

        with open(input_file, 'r') as input_stream:
            self.input = input_stream.read()
            return self.input

