#!/usr/bin/python3
"""
    This module containe a single  function that read files
"""


def read_file(filename=""):
    """
        print the content of a file
        Prams:
            string : filename
        Return:
            void
    """
    with open(filename, 'r') as f:
        content = f.read()
        print(content, end="")
