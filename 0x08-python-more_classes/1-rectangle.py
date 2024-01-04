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
        self.handleParams("width", width)
        self.handleParams("height", height)
        self.height = height
        self.width = width

    def __getattr__(self, name):
        """
        Overrides the __getattr__ method
        to retrieve attributes in a specific way.

        Parameters:
        - name (str): The name of the attribute.

        Returns:
        - The value of the attribute.
        """
        return self.__dict__[f"__{name}"]

    def __setattr__(self, name, value):
        """
        Overrides the __setattr__ method to set attributes in a specific way.

        Parameters:
        - name (str): The name of the attribute.
        - value: The value to set for the attribute.
        """
        if name == "width":
            self.handleParams(name, value)
        if name == "height":
            self.handleParams(name, value)
        self.__dict__[f"__{name}"] = value

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
