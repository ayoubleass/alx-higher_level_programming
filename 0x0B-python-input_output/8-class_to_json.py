#!/usr/bin/python3
"""
    This module define a function
    that return serialize an object to a dictionary
"""


import json


def class_to_json(obj):
    """
    Serialize an object to a dictionary.
    """

    if hasattr(obj, '__dict__'):
        return obj.__dict__
    return json.dumps(obj)
