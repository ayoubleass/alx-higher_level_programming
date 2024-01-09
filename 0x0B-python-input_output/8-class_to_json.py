#!/usr/bin/python3
"""
    Serialize an object to a dictionary.
"""


import json


def class_to_json(obj):
    """
    Serialize an object to a dictionary.
    """
    if isinstance(obj, object):
        return json.dumps(obj.__dict__)
