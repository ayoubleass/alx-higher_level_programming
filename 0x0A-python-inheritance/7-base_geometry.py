#!/usr/bin/python3
"""
    This module define class BaseGeometry
"""


class BaseGeometry:
    """
        Base class that implements certain
        attributes that the child class will need
    """

    def area(self):
        """
            Raise Exception
        """
        raise Exception("is not implemented")

    def integer_validator(self, name, value):
        """
            check if value is integer.
            check if value is less or equal then 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
