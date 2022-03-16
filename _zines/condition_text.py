import frontmatter
import glob
import re
import sys

BASEURL = "https://manyworldspod.github.io/assets/img/{}"


# -- utilities ----------------------------------------------------------------


def _get_post_file(stub):
    """Locate a post's markdown file from its stub"""
    files = glob.glob(f"../_posts/*{stub}.md")
    if not files:
        raise FileNotFoundError(f"Could not locate file with stub {stub}")
    elif len(files) > 1:
        raise ValueError(f"Multiple files located with stub {stub}")
    return files[0]


def capture_post_figures(text):
    """Given the original post's markdown, capture its figures throughout"""
    text = re.sub("\{\% assign(.+?)\%\}", "", text)
    # replace {% include ... %} statements with markdown
    for image in frontmatter.loads(text)["images"]:
        md = f"![{image['alt']}]({BASEURL}/{image['url']})"
        text = re.sub("\{\%(.+?)\%\}", md, text, count=1)
    return text


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
    # read the post's original markdown
    BASEURL = BASEURL.format(sys.argv[1])
    with open(_get_post_file(sys.argv[1]), "r") as fobj:
        contents = fobj.read()

    # strip out formatting that makes sense on the website, but not
    # in a printed zine, and account for footnotes within captions
    contents = separate_figure_caption_footnotes(
        capture_post_figures(
            contents.replace("\n\n---", "")
        )
    )

    # write the conditioned markdown
    with open("source.md", "w") as fobj:
        fobj.write(contents)
