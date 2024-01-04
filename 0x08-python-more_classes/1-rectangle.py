#!/usr/bin/python3
"""
    This module  is rectanngle class
"""


class Rectangle:
    """
    A class representing a rectangle with width and height.

    Attributes:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle object with the specified width and height.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.handleParams("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.handleParams("height", value)
        self.__height = value

    def handleParams(self, name, value):
        """
        Validates and handles parameters for width and height.

        Parameters:
        - name (str): The name of the parameter.
        - value: The value of the parameter.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value < 0:
            raise ValueError("{:s} must be >= 0".format(name))
