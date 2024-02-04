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


def update_image_paths(contents, images, current_directory):
    # replace all image paths ![[file.ext]] with ![[relative/path/to/file.ext]]
    # images[0].relative_to(current_directory)

    # extract all ![[file.ext]] from the contents
    to_replace = re.findall(r"!\[\[.*\]\]", contents)
    for image in to_replace:
        image_name = image[3:-2]
        image_path = pathlib.Path(image_name)
        # ! crashes if the image is not found
        image_path = image_path.relative_to(current_directory)
        contents = re.sub(
            r"!\[\[" + image_name + r"\]\]",
            r"![[" + str(image_path) + r"]]",
            contents,
        )

    for image in images:
        image_name = image.name
        image_path = image.relative_to(current_directory)
        contents = re.sub(
            r"!\[\[" + image_name + r"\]\]",
            r"![[" + str(image_path) + r"]]",
            contents,
        )
    return contents


# get all files in the directory and its subdirectories
path = "./test"
path = pathlib.Path(path)

# create map with all file names and their relative paths
md_files = []
images = []
for r, d, f in os.walk(path):
    for file in f:
        file_extension = os.path.splitext(file)[1]
        if file_extension == ".md":
            md_files.append(pathlib.Path(os.path.join(r, file)))
        elif file_extension in [".png", ".jpg", ".jpeg", ".gif"]:
            images.append(pathlib.Path(os.path.join(r, file)))


for file_path in md_files:
    with open(file_path, "r") as file:
        contents = file.read()

    contents = remove_header(contents)
    contents = update_image_paths(contents, images, file_path.parent)

    # write the new contents to the file
    exit()
    with open(file_path, "w") as file:
        file.write(contents)
