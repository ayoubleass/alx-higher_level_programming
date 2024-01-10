#!/usr/bin/python3
"""
    This module define Rectangle class
"""

mod = __import__("7-base_geometry")


class Rectangle(mod.BaseGeometry):
    """
    This class define Rectangle
    """

    def __init__(self, width, height):
        """
        validate the params and bind them to the object/instance
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
