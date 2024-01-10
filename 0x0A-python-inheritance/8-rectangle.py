#!/usr/bin/python3
"""
    This modeule define Rectangle class
"""


class Rectangle:
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
