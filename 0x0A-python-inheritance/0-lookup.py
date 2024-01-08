#!/usr/bin/python3
"""
    This modeule is a function that return a list
    containing attribute and methods of the passed object
"""


def lookup(obj):
    """
        Params:
            object : obj
        Return:
            a list containing attribute and methods of the passed object
    """

    object_attr = [element for element in dir(obj)]
    return object_attr
