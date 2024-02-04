# sudo apt install texlive-latex-recommended
# sudo apt install pandoc
import os


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


pandoc = 'pandoc -H tools/head.tex --pdf-engine=pdflatex "../FILENAME.md" -o "../pdf/FILENAME.pdf" -s -V fontsize=12pt -V geometry:"top=2cm, bottom=1.5cm, left=2cm, right=2cm" --resource-path="../"'
path = "../"
md_files = get_md_files(path)
for md_file in md_files:
    os.makedirs("../pdf/" + extract_parent_folder(md_file), exist_ok=True)
    os.system(pandoc.replace("FILENAME", str(md_file)))
