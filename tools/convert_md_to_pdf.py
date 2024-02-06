# sudo apt install texlive-latex-recommended
# sudo apt install pandoc
# python3 convert_md_to_pdf.py -sf ../ -df ../pdf/ -th ../tools/head.tex -r ../z_images
import os
import subprocess
import argparse


def handle_args():

    parser = argparse.ArgumentParser(description="Convert markdown files to pdf")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Prints more information"
    )
    parser.add_argument("-sf", "--source-folder", help="Path to the source folder")
    parser.add_argument(
        "-df", "--destination-folder", help="Path to the destination folder"
    )
    parser.add_argument("-sfile", "--source-file", help="Path to source file")
    parser.add_argument("-dfile", "--destination-file", help="Path to destination file")
    parser.add_argument("-th", "--tex-header-file", help="Path to tex header file")
    parser.add_argument("-r", "--resource-path", help="Resource path for images")
    args = parser.parse_args()

    folder_mode = True if args.source_folder and args.destination_folder else False

    if folder_mode or (args.source_file and args.destination_file):
        return args, folder_mode
    parser.print_help()
    parser.error(
        "Please provide either source and destination folders or source and destination files"
    )


def create_pandoc_command(args):
    pandoc = 'pandoc --pdf-engine=xelatex -s -V fontsize=12pt -V geometry:"top=2cm, bottom=1.5cm, left=2cm, right=2cm"'
    if args.resource_path:
        pandoc += ' --resource-path="' + args.resource_path + '"'
    if args.tex_header_file:
        pandoc += ' -H "' + args.tex_header_file + '"'
    if folder_mode:
        if args.source_folder[-1] != "/":
            args.source_folder += "/"
        if args.destination_folder[-1] != "/":
            args.destination_folder += "/"
        pandoc += (
            ' "'
            + args.source_folder
            + 'FILENAME.md" -o "'
            + args.destination_folder
            + 'FILENAME.pdf"'
        )
    else:
        pandoc += ' "' + args.source_file + '" -o "' + args.destination_file + '"'
    return pandoc


def get_md_files(path):
    md_files = []
    for r, d, f in os.walk(path):
        for file in f:
            file_extension = os.path.splitext(file)[1]
            if file_extension == ".md":
                md_files.append(os.path.join(r, file)[3:-3])  # remove .md
    return md_files


def extract_parent_folder(file):
    last_slash = md_file.rfind("/")
    last_slash = last_slash if last_slash != -1 else 0
    return file[:last_slash]


if __name__ == "__main__":
    args, folder_mode = handle_args()
    pandoc = create_pandoc_command(args)
    if args.verbose:
        print(pandoc)
    if folder_mode:
        md_files = get_md_files(args.source_folder)
        failed_files = []
        if args.verbose:
            print("Found " + str(len(md_files)) + " markdown files")
        for md_file in md_files:
            if args.verbose:
                print("Converting " + md_file)
            os.makedirs("../pdf/" + extract_parent_folder(md_file), exist_ok=True)
            output = subprocess.run(
                pandoc.replace("FILENAME", str(md_file)),
                shell=True,
                capture_output=True,
            )
            if output.returncode != 0:
                failed_files.append((md_file, output.stderr))

        if len(failed_files) > 0:
            print("\nFailed to convert " + str(len(failed_files)) + " files")
            print("Check failed_files.txt for more information")
            with open("failed_files.txt", "w") as file:
                for failed_file in failed_files:
                    file.write(failed_file[0] + "\n")
                    file.write(failed_file[1].decode("utf-8") + "\n")
    else:
        output = subprocess.run(pandoc, shell=True, capture_output=True)
        if args.verbose:
            print(output)
