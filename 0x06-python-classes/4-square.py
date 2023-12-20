#!/usr/bin/python3
"""
This module defines the Square class.
"""


def raiseError(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")


class Square:
    """
    Initializes a new instance of the Square class.

    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        raiseError(value)
        self.__size = value

    def area(self):
        """
        Returns the current square area
        """
        return self.__size * self.__size
