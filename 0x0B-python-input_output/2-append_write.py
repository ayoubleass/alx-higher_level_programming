#!/usr/bin/python3
"""
    This script defines a function to append  text to a file.
"""


def append_write(filename="", text=""):
    """
        append_write: Append  text to a file
    """

    size = 0
    with open(filename, "a") as f:
        size = f.write(text)
    return size
