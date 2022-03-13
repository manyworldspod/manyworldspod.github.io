# Automagic zine publication

This folder contains a suite of tools that export, format, and ultimately
publish zines based on articles posted to the website. The zines are printed
on A4 paper, [imposed](https://en.wikipedia.org/wiki/Imposition) such that one
sheet of paper contains two pages per side.

## Installation

To use this software, you will need a command-line environment with the
following packages installed:

* [PDFLaTeX](https://www.latex-project.org/get/)
* [Pandoc](https://pandoc.org/installing.html)

You will also need a [Python](https://www.python.org/) interpreter, for our
purposes any currently supported version will do.

## Optional: blurb for the back cover

If there is text you'd like to include as a blurb on the zine's back cover, you
can write it to a file called `blurb.md`, with all the markdown formatting you
like. For example,


```markdown
This is a sentence with some _emphatic ideas_ and some *bold claims*.
```

will be rendered as:

> This is a sentence with some _emphatic ideas_ and some *bold claims*.

Note, if your blurb is longer than a paragraph you will have to format it by
hand with HTML tags.

## Render the imposed PDF

Now you are ready to publish a zine. To do this you'll need your post's stub,
the shortname it's filed under online. For example, the article published at
https://manyworldspod.github.io/restorative-justice-northeast-syria has the
stub `restorative-justice-northeast-syria`.

On the command-line, navigate to this folder and run the following:

```bash
make <stub>
```

where `<stub>` is the one corresponding to your article. To take the same
example again, this would look like

```bash
make restorative-justice-northeast-syria
```

This will publish an imposed PDF of your zine under `/assets/zines/<stub>.pdf`,
from the repository's top-level directory. If your article cites references
via hyperlink, those links will be captured and written out in full as
footnotes wherever they're cited.

### But wait!

Before you share your zine publicly, you'll want to compare the output of the
imposed version (`/assets/zines/<stub>.pdf`) to the raw version (`raw.pdf` in
this directory). If something seems off, _e.g._ there are pages missing, it's
likely because of a setting in `impose.tex`. If you open that file and go to
[line 22](https://github.com/manyworldspod/manyworldspod.github.io/blob/main/_zines/impose.tex#L22)
you will find it:

```tex
\includepdf[pages=-,signature=28,landscape]{raw.pdf}
```

You'll want to make sure the `signature` argument matches the number of pages
in `raw.pdf`, which should always be an even number.

This is the only known point of failure in zine publication. If you find
another one, or if you have a feature request, please post an
[issue ticket](https://github.com/manyworldspod/manyworldspod.github.io/issues).

## For my fellow nerds: what's happening under the hood?

The `Makefile` implements a 4-step process:

1. Export the article published online to a local markdown file
2. Remove junk from the website's header and footer, reformat source links
   inside of figure captions, clean up extraneous things that make sense on
   a website but not in a PDF, and (optionally) include a blurb for the back
   cover
3. Export the markdown to a regular, report-style, one-page-at-a-time PDF
4. Impose the PDF four pages to a sheet (two on the front, two on the back)
   and save it in the right location to be discoverable on the website

Steps 1 and 3 require Pandoc, step 2 requires Python, and steps 3 and 4 require
PDFLateX. If you want to clean up all the scratch work from these steps, you
can simply run

```bash
make clean
```

When you're ready to publish to the website, make sure you're on a scratch
branch, push to `origin/<branch>` and open a pull request.

### Why do we need another markdown file? Didn't I post from a markdown to begin with...?

Yep! And I apologize for the confusion. Another markdown is needed to properly
capture images after they're published to the website. Pandoc's LaTeX engine
knows how to take these and ship them with the final PDF.
