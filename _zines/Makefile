# Makefile to convert published articles into nicely formatted zines
# NOTE: this requires Pandoc and PDFLaTeX in the run environment

%:
	# convert the formatted web post back to markdown
	# this is done to properly capture images, captions, and links
	- pandoc -s -r html https://manyworldspod.github.io/$@ -o $@.md
	# remove vestiges of the website's header and footer,
	# and do a few other minor formatting enhancements
	- python -m condition_text $@.md
	# convert the markdown to PDF
	- pandoc $@.md --defaults defaults.yml -o raw.pdf
	# finally, impose two script pages per A4 page
	# NOTE: please check the settings in impose.tex for this article
	- pdflatex impose && mv impose.pdf ../assets/zines/$@.pdf

clean:
	# remove intermediate publishing products
	- find . -maxdepth 1 ! -name "README.md" -name "*.md" -delete
	- rm -rf __pycache__ *.{aux,log,pdf}
