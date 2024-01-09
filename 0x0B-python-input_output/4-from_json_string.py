#!/usr/bin/python3
"""
    This script define a function that
    Returns the Python object represented by the provided JSON string.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object represented by the provided JSON string.
    """
    return json.loads(my_str)
