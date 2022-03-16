# Automagic zine publication

This folder contains a suite of tools that export, format, and ultimately
publish zines based on articles posted to the website. The zines are printed
on A4 paper, [imposed](https://en.wikipedia.org/wiki/Imposition) such that one
sheet of paper contains two pages per side (four total).

## Installation

To use this software, you will need a command-line environment with the
following packages installed:

* [PDFLaTeX](https://www.latex-project.org/get/)
* [Pandoc](https://pandoc.org/installing.html)
* [python-frontmatter](https://pypi.org/project/python-frontmatter/)

You will also need a [Python](https://www.python.org/) interpreter, for our
purposes any currently supported version will do.

## Optional: blurb for the back cover

If there is text you'd like to include as a blurb on the zine's back cover,
you can write it to a frontmatter variable called `blurb` with all the usual
markdown formatting. For example,


```markdown
blurb: >-
  This is a sentence with some _emphatic ideas_ and some **bold claims**.
```

will be rendered as:

> This is a sentence with some _emphatic ideas_ and some **bold claims**.

## Render the imposed PDF

Now you are ready to publish a zine! To do this you'll need your post's slug,
the shortname it's filed under online. For example, the article published at
https://manyworldspod.github.io/restorative-justice-northeast-syria has the
slug `restorative-justice-northeast-syria`.

On the command-line, navigate to this folder and run the following:

```bash
make <slug>
```

where `<slug>` is the one corresponding to your article. To take the same
example again, this would look like

```bash
make restorative-justice-northeast-syria
```

This will publish an imposed PDF of your zine under `/assets/zines/<slug>.pdf`,
from the repository's top-level directory.

Some other notes:

* If your article cites references via hyperlink, those links will be captured
  and written out in full as footnotes wherever they're cited.
* The final zine will include boilerplate text about the podcast on the inside
  front cover, followed by a table of contents. The back cover will always fall
  on an even-numbered page; if it's on an odd-numbered page, then a blank page
  will be inserted right before it.

### But wait!

Before you share your zine publicly, you should compare the draft of the
imposed version (`/assets/zines/<slug>.pdf`) to the raw version (`raw.pdf` in
this directory). If something seems off, _e.g._ there are pages missing, it's
likely because of a setting in `impose.tex`. You'll find it if you open that
file and go to
[line 22](https://github.com/manyworldspod/manyworldspod.github.io/blob/main/_zines/impose.tex#L22):

```tex
\includepdf[pages=-,signature=28,landscape]{raw.pdf}
```

You'll want to make sure the `signature` argument matches the number of pages
in `raw.pdf`, which should always be an even number.

This is the only known point of failure in zine publication. If you find
another one, or if you have a feature request, please post an
[issue ticket](https://github.com/manyworldspod/manyworldspod.github.io/issues).

## For my fellow nerds: what's happening under the hood?

The `Makefile` implements a 3-step process:

1. Condition the original markdown, _i.e._ capture all figures (including
   captions and placement) and format the text for publication as a zine
2. Export the markdown to a regular, report-style, one-page-at-a-time PDF
3. Impose the PDF four pages to a sheet (two on the front, two on the back)
   and save it in the correct location to be discoverable on the website

Step 1 requires Python, step 2 requires Pandoc, and steps 2 and 3 require
PDFLateX. If you want to clean up all the scratch work from these steps, you
can simply run

```bash
make clean
```

When you're ready to publish to the website, make sure you're on a bespoke
branch, then push to `origin/<branch>` and open a pull request.
