#!/usr/bin/python3
"""
    This modeule is a function that return a list containing attribute and methods of the passed object
"""
def lookup(obj):
    object_attr = [element for element in dir(obj)]
    return object_attr
