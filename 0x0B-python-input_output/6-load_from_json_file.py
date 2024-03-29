#!/usr/bin/python3
"""
    This is a skript with a function
    that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.
    """
    with open(filename, "r") as f:
        return json.load(f)
