%:
	- pandoc -s -r html https://manyworldspod.github.io/$@ -o $@.md
	- pandoc $@.md -o $@.pdf

clean:
	- rm -f *.{md,pdf}
