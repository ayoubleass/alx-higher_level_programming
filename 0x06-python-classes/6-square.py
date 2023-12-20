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

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or 
        len(value) != 2 or
        not all(isinstance(n, int) for n in value) or
        not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size > 0:
            x, y = self.__position
            for i in range(0, self.__size):
                j = 0
                while j < self.__size:
                    if not y < 0 and j == 0:
                        print(' ' * x, end="")
                    print("#", end="")
                    j += 1
                print()
        else:
            print()
