#!/usr/bin/python3
"""
    This module has only one function that check
    if is the  first param is an instance of the second one
"""


def is_kind_of_class(obj, a_class):
    """
        check is the fits param is an instance of the second one
    """
    return isinstance(obj, a_class)
