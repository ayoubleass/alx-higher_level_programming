#!/usr/bin/python3
"""
    skript that define a function that returns
    the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of the provided object (string).

    Parameters:
        - my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
