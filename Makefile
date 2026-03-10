.PHONY: all clean

all: paper/paper.pdf

# Preprocessing: data wrangling and figures
output/figures/figure_5_2.png output/figures/figure_5_3.png: input/PaidSearch.csv code/preprocess.py
	USERPROFILE=C:/Users/patrick HOMEDRIVE=C: HOMEPATH=/Users/patrick python code/preprocess.py

# DID estimation
output/tables/did_table.tex: input/PaidSearch.csv code/did_analysis.py
	USERPROFILE=C:/Users/patrick HOMEDRIVE=C: HOMEPATH=/Users/patrick python code/did_analysis.py

# Paper compilation
paper/paper.pdf: paper/paper.tex output/figures/figure_5_2.png output/figures/figure_5_3.png output/tables/did_table.tex
	cd paper && pdflatex paper.tex && pdflatex paper.tex

clean:
	rm -f output/figures/*.png output/tables/*.tex paper/paper.pdf paper/paper.aux paper/paper.log



# Task 2 Answers
# 1. If you edit code/preprocess.py, which targets will Make rebuild? Which targets will it skip?
# Rebuild: output/figures/figure_5_2.png, output/figures/figure_5_3.png, paper/paper.pdf
# Skip: output/tables/did_table.tex
#
# 2. If you edit code/did_analysis.py, which targets will Make rebuild? Which targets will it skip?
# Rebuild: output/tables/did_table.tex, paper/paper.pdf
# Skip: output/figures/figure_5_2.png, output/figures/figure_5_3.png
#
# 3. If you edit paper/paper.tex, which targets will Make rebuild? Which targets will it skip?
# Rebuild: paper/paper.pdf
# Skip: output/figures/figure_5_2.png, output/figures/figure_5_3.png, output/tables/did_table.tex
