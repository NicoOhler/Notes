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

# create map with all file names and their relative paths
md_files = []
files = {}
for file in list(directory.iterdir()):
    if file.is_file():
        files[file.name] = file.relative_to(directory)
        if file.suffix == ".md":
            md_files.append(file)


# iterate over all markdown files
for file_path in files:
    if file_path.suffix != ".md":
        continue

    with open(file_path, "r") as file:
        contents = file.read()

    # replace each link with the relative path from map
    new_contents = contents
    for file_name in files:
        new_contents = re.sub(
            r"\[\[" + file_name + r"\]\]",
            r"[[./" + str(files[file_name]) + r"]]",
            new_contents,
        )

    # add ".md" to all links that don't have an extension
    new_contents = re.sub(r"\[\[(.*?)\]\]", r"[[\1.md]]", new_contents)

    # write the new contents to the file
    with open(file_path, "w") as file:
        file.write(new_contents)
