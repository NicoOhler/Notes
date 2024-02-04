# sudo apt install texlive-latex-recommended
# sudo apt install pandoc
import os

pandoc = 'pandoc -H ../tools/head.tex --pdf-engine=pdflatex FILENAME.md -o FILENAME.pdf --s -V geometry:"top=2cm, bottom=1.5cm, left=2cm, right=2cm"'
