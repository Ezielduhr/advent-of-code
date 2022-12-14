#!/usr/bin/env python3
from git import Repo as git_repo
from os import path as os_path

repo_root = os_path.realpath(git_repo(__file__, search_parent_directories=True).working_tree_dir)


def get_input(file_name, path_to_file=f"2022/library/input"):
    input_file = f"{repo_root}/{path_to_file}/{file_name}"

    with open(input_file, 'r') as input_stream:
        return input_stream.readlines()
