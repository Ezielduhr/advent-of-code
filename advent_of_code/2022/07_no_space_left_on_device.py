#!/usr/bin/evn python3
from library.shared_functions import get_input
from anytree import Node, RenderTree

all_instances = {}


class Directory(Node):
    """ This class uses the anytree node class as base to create a tree structure of the input directories """
    def __init__(self, name, id=None, parent=None, children=None, **kwargs):
        super().__init__(name, parent, children, **kwargs)
        self._files = []
        self.dir_size = 0
        all_instances[id] = self

    def add_files(self, files):
        size, file_name = files
        self._files.append([size, file_name])
        self.update_size(size)

    def update_size(self, size):
        for instance in self.path:
            instance.dir_size += int(size)


class DirectoryCursor:
    """ This class contains the information we need to move around a directory like data structure """
    def __init__(self):
        self.pwd = 'root'
        self.current_directory = 'root'
        self.parent = None

    def change_directory(self, command):
        if command == '/' or (command == '..' and self.pwd.count('_') == 1):
            self.pwd = 'root'
            self.current_directory = 'root'
            self.parent = None

        elif command == '..':
            self.current_directory = self.pwd.split('_')[-2:-1][0]
            self.parent = self.pwd.split('_')[-3:-2][0]
            self.pwd = '_'.join(self.pwd.split('_')[:-1])

        else:
            self.current_directory = command
            self.parent = self.pwd
            if self.pwd == 'root':
                self.pwd = f"root_{command}"
            else:
                self.pwd = f"{self.pwd}_{command}"


def main():
    """ This function goes through a list of "bash" instructions and moves around directories while listing files
     and tracking memory sizes for directories and files.
     In "part 2" we find the amount of memory we need to free up for some software update
     and the smallest directory size that would accommodate that.
    Note: Cheating a bit by assuming a line containing numbers or the word dir is prefaced by a `ls` command
        useful info on Trees in Python: https://medium.com/swlh/making-data-trees-in-python-3a3ceb050cfd """

    challenge_input = get_input("input_07.txt")

    # This cursor class is used to keep te relative information of the directories
    cursor = DirectoryCursor()
    # Initialize root directory
    Directory(cursor.current_directory, id=cursor.pwd)

    for line in challenge_input:
        instruction = line.replace('\n', '').split()

        # Check if first element is:
        # a command
        if instruction[0] == '$':
            if len(instruction) == 3:
                useless, command, argument = instruction
                if command == 'cd':
                    cursor.change_directory(argument)

                    # check if Directory instance exists
                    if cursor.pwd in all_instances:
                        pass
                    # create Directory instance if it doesn't already exist
                    else:
                        Directory(cursor.current_directory, id=cursor.pwd, parent=all_instances.get(cursor.parent))

        # a file
        elif instruction[0].isnumeric():
            # add file to pwd
            all_instances[cursor.pwd].add_files(instruction)

        # a dir
        elif instruction[0] == 'dir':
            # check if instance exists

            new_dir = f"{cursor.pwd}_{instruction[1]}"
            if new_dir in all_instances:
                pass
            else:
                # create instance
                Directory(instruction[1], id=new_dir, parent=all_instances[cursor.pwd])
        else:
            raise ValueError('Instruction not recognised, please report to your nearest overseer elf')

    weird_total_memory = sum([instance.dir_size for instance in all_instances.values() if instance.dir_size <= 100000])

    # Part 2
    total_system_memory = 70000000
    required_memory_for_update = 30000000
    free_memory = total_system_memory - all_instances['root'].dir_size
    needed_memory = required_memory_for_update - free_memory

    smallest_dir_which_we_can_miss_i_hope = min(
        [instance.dir_size for instance in all_instances.values() if instance.dir_size >= needed_memory])

    return weird_total_memory, smallest_dir_which_we_can_miss_i_hope, RenderTree(all_instances['root'])


if __name__ == "__main__":
    total_memory, memory_to_clean, tree = main()
    print(f"fancy tree: {tree}")
    print(f"fancy tree: {tree} \n \
    sum of memory of dirs that have / or more then 100000 = {total_memory},\n \
     memory of smallest dir that can be removed to allow the update {memory_to_clean}")
