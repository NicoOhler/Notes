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


def remove_header(contents):
    # remove first line if it starts with "# "
    if contents.startswith("# "):
        contents = contents[contents.find("\n") + 1 :]
    return contents


def update_image_paths(contents, images):
    # replace all image paths
    for image in images:
        image_name = image.name
        image_path = str(image.relative_to(directory))
        contents = contents.replace(image_name, image_path)
    return contents


# get all files in the directory and its subdirectories
directory = "./test"
directory = pathlib.Path(directory)

# create map with all file names and their relative paths
md_files = []
images = []
for file in list(directory.iterdir()):
    if file.is_file():
        if file.suffix == ".md":
            md_files.append(file)
        elif file.suffix in [".png", ".jpg", ".jpeg", ".gif", ".svg"]:
            images.append(file)


for file_path in md_files:
    with open(file_path, "r") as file:
        contents = file.read()

    contents = remove_header(contents)

    # write the new contents to the file
    with open(file_path, "w") as file:
        file.write(contents)
