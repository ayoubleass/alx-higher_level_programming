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
