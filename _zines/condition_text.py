import os
import re
import sys


# -- utilities ----------------------------------------------------------------


def _preserve_publish_date(text):
    """Ensure the publish date is recorded in metadata"""
    date = re.findall("published (.*)", text)[0]
    return re.sub("generator: (.*)", f"postdate: {date}", text)


def remove_html_header_and_footer(text):
    """Remove vestiges of HTML header and footer from the given text"""
    header = re.compile(":::(.*)post\-date}", re.DOTALL)
    footer = re.compile("::: {\.post\-share}(.*):::", re.DOTALL)
    beheaded = re.sub(header, "", text)
    return re.sub(footer, "", beheaded)


def separate_figure_caption_footnotes(text):
    """Prepare source markdown to separate footnotes from figure captions"""
    hits = re.findall(
        "source:(.+?)\[(.+?)\]\((.+?)\)", text, re.DOTALL
    )
    for (_, source, url) in hits:
        text = (
            text
            .replace(f"[{source}]", f"{source}^")
            .replace(f"({url})", f"[`{url}`]")
        )
    return text


# -- main block ---------------------------------------------------------------


if __name__ == "__main__":
    # read Pandoc's original markdown
    with open(sys.argv[1], "r") as fobj:
        contents = _preserve_publish_date(fobj.read())

    # strip out formatting that makes sense on the website, but not
    # in a printed zine, and account for footnotes within captions
    contents = separate_figure_caption_footnotes(
        remove_html_header_and_footer(
            contents
            .replace(" \| Where Many Worlds Fit", "") \
            .replace("----", "")
        )
    )

    blurb = ""  # if a blurb is available, use it
    if os.path.exists("blurb.md"):
        with open("blurb.md") as fobj:
            blurb = fobj.read().replace("\n", " ")

    # overwrite the original file
    with open(sys.argv[1], "w") as fobj:
        fobj.write(
            re.sub(
                "description: (.*)",
                f"description: \"{blurb}\"",
                contents
            )
        )
