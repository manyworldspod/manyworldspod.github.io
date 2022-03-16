# Makefile to convert published articles into nicely formatted zines
# NOTE: this requires Pandoc and PDFLaTeX in the run environment

%:
	# capture figures with captions, and
	# other minor formatting enhancements
	- python -m condition_text $@
	# convert the markdown to PDF
	- pandoc source.md --defaults defaults.yml -o raw.pdf
	# finally, impose two script pages per A4 page
	# NOTE: please check the settings in impose.tex for this article
	- pdflatex impose && mv impose.pdf ../assets/zines/$@.pdf

clean:
	# remove intermediate publishing products
	- find . -maxdepth 1 ! -name "README.md" -name "*.md" -delete
	- rm -rf __pycache__ *.{aux,log,pdf}
