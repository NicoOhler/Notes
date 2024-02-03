# replaces paths like [[file]] with [[relative/path/to/file.ext]] in all markdown files of a given directory and its subdirectories

import os
import re
import glob
import sys

directory
directory = sys.argv[1]
if not os.path.isdir(directory):
    print("The given directory does not exist.")
    sys.exit(1)


# get all files in the current directory and its subdirectories
files = glob.glob(directory, recursive=True)

# iterate over all markdown files
for file_path in files:
    # open the file and read the contents
    with open(file_path, "r") as file:
        contents = file.read()

    # replace all paths with the relative path
    relative_path = os.path.relpath(file_path, os.getcwd())
    new_contents = re.sub(
        r"\[\[(.*?)\]\]", r"[[{}/\1]]".format(relative_path), contents
    )

    # write the new contents to the file
    with open(file_path, "w") as file:
        file.write(new_contents)
