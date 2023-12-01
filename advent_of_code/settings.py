import git
from pathlib import Path

repo_root = Path(git.Repo('.', search_parent_directories=True).working_tree_dir)
