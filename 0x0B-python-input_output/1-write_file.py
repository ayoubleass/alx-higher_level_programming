#!/usr/bin/python3
"""
    This script defines a function to write text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes the provided text to the specified file.

    Parameters:
        - filename (str): The name of the file to write to.
        - text (str): The text to be written to the file.
    """
    size = 0
    with open(filename, "w") as f:
        size = f.write(text)
    return size
