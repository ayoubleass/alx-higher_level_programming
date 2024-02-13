#!/usr/bin/python3
"""
Module for add_integer
"""


def add_integer(a, b=98):
    """
    Args:
        a: integer or float
        b: ineger or float
    Returns:
        the addition of a and b
    """

    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    from doctest import testfile
    testfile("tests/0-add_integer.txt")
