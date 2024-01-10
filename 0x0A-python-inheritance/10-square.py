#!/usr/bin/python3
"""
     This modeule define  a class Square
"""

mod = __import__("9-rectangle")


class Square(mod.Rectangle):

    def __init__(self, size):
        """
        Initializes a Square instance with a size.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Compute de size of a square
        """
        return self.__size * self.__size
