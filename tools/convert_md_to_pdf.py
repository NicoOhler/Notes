# sudo apt install texlive-latex-recommended
# sudo apt install pandoc
import os


def get_md_files(path):
    md_files = []
    for r, d, f in os.walk(path):
        for file in f:
            file_extension = os.path.splitext(file)[1]
            if file_extension == ".md":
                md_files.append(os.path.join(r, file))
    return md_files


pandoc = 'pandoc -H ../tools/head.tex --pdf-engine=pdflatex FILENAME.md -o FILENAME.pdf --s -V geometry:"top=2cm, bottom=1.5cm, left=2cm, right=2cm"'
path = "../"
md_files = get_md_files(path)
for md_file in md_files:
    os.system(pandoc.replace("FILENAME", str(md_file)))
