# "Usage: python3 update_paths.py <directory>"

import os
import re
import sys
import pathlib


def handle_args():
    if len(sys.argv) != 2:
        print("Usage: python3 update_paths.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("The given directory does not exist.")
        sys.exit(1)

    return pathlib.Path(directory)


def get_md_and_images(path):
    md_files = []
    images = []
    for r, d, f in os.walk(path):
        for file in f:
            file_extension = os.path.splitext(file)[1]
            if file_extension == ".md":
                md_files.append(pathlib.Path(os.path.join(r, file)))
            elif file_extension in [".png", ".jpg", ".jpeg", ".gif"]:
                images.append(pathlib.Path(os.path.join(r, file)))
    return md_files, images


def remove_header(contents):
    # remove first line if it starts with "# "
    if contents.startswith("# "):
        contents = contents[contents.find("\n") + 1 :]
    return contents


def create_relative_image_paths(contents, images, current_file):
    # replace all image paths ![[file.ext]] with ![[relative/path/to/file.ext]]
    # extract all ![[file.ext]] from the contents
    to_replace = re.findall(r"!\[\[.*\]\]", contents)
    for image in to_replace:
        image_name = image[3:-2]
        if "/" in image_name:
            continue

        # find the image in the images list
        image_path = None
        for img in images:
            if img.name == image_name:
                image_path = str(img)

        if image_path is None:
            print("Image not found: " + image_name + " in " + str(current_file))
            continue

        image_path = os.path.relpath(image_path, current_file.parent)

        contents = re.sub(
            r"!\[\[" + image_name + r"\]\]",
            r"![[" + str(image_path) + r"]]",
            contents,
        )

    return contents


def convert_to_md_path(contents):
    # replace all ![[Pasted Image.png]] with !()[Pasted%20Image.png]
    to_replace = re.findall(r"!\[\[.*\]\]", contents)
    for image in to_replace:
        image_name = image[3:-2]

        image_name_url_encoded = image_name.replace(" ", "%20")

        contents = re.sub(
            r"!\[\[" + image_name + r"\]\]",
            r"!()[" + image_name_url_encoded + r"]",
            contents,
        )

    return contents


if __name__ == "__main__":
    # path = handle_args()
    path = "../"
    md_files, images = get_md_and_images(path)
    for file_path in md_files:
        with open(file_path, "r") as file:
            contents = file.read()

        contents = remove_header(contents)
        contents = create_relative_image_paths(contents, images, file_path)
        contents = convert_to_md_path(contents)

        # write the new contents to the file
        with open(file_path, "w") as file:
            file.write(contents)
