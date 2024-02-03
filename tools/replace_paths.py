# replaces paths like [[file]] with [[relative/path/to/file.ext]] in all markdown files of a given directory and its subdirectories

import os
import re
import sys
import pathlib

"""
if len(sys.argv) != 2:
    print("Usage: python replace_paths.py <directory>")
    sys.exit(1)

directory = sys.argv[1]
if not os.path.isdir(directory):
    print("The given directory does not exist.")
    sys.exit(1)
"""

# get all files in the directory and its subdirectories
directory = "./test"
directory = pathlib.Path(directory)
files = list(directory.iterdir())


# iterate over all markdown files
for file_path in files:
    if file_path.suffix != ".md":
        continue

    with open(file_path, "r") as file:
        contents = file.read()

    # replace all paths with the relative path
    relative_path = os.path.relpath(file_path, os.getcwd())
    new_contents = re.sub(
        r"\[\[(.*?)\]\]", r"[[{}/\1]]".format(relative_path), contents
    )

    # add ".md" to all links that don't have an extension
    new_contents = re.sub(r"\[\[(.*?)\]\]", r"[[\1.md]]", new_contents)

    # write the new contents to the file
    with open(file_path, "w") as file:
        file.write(new_contents)
