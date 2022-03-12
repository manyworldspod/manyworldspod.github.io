# Makefile to convert published articles into nicely formatted zines
# NOTE: this requires Pandoc and PDFLaTeX in the run environment

%:
	# convert the formatted web post back to markdown
	# this is done to properly capture images, captions, and links
	- pandoc -s -r html https://manyworldspod.github.io/$@ -o $@.md
	# remove vestiges of the website's header and footer
	- sed -i '' '10,40d' $@.md
	- sed -n -e :a -e '1,28!{P;N;D;};N;ba' -i '' $@.md
	# convert the markdown to PDF
	- pandoc $@.md --defaults defaults.yml -o $@.pdf

clean:
	# remove intermediate publishing products
	- rm -f *.{md,pdf}
