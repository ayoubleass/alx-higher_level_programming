#!/usr/bin/python3
"""
    This module has a function that
    check if the obj base class is the a subclass of a_class
"""


def inherits_from(obj, a_class):
    """
        check if the obj base class is the a subclass of a_class
    """
    return issubclass(type(obj),  a_class)
