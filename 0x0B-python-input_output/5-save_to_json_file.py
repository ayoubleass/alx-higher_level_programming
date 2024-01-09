#!/usr/bin/python3
"""
    This skript define a function
    that writes an Object to a text file, using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
        Writes the JSON representation of the provided object to a text file.
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
