import re
import sys


# -- utilities ----------------------------------------------------------------


def remove_header_and_footer(text):
    """"""
    header = re.compile(":::(.*)post\-date}", re.DOTALL)
    footer = re.compile("::: {\.post\-share}(.*):::", re.DOTALL)
    cleaned = re.sub(header, "", text)
    return re.sub(footer, "", cleaned)


# -- main block ---------------------------------------------------------------


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fobj:
        text = fobj.read()
    with open(sys.argv[1], "w") as fobj:
        fobj.write(
            remove_header_and_footer(text)
        )
