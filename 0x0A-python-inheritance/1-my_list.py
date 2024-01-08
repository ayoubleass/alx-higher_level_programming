#!/usr/bin/python3
"""
    This module conntaine a subclass of the list class
"""


class MyList(list):
    """
        This class is a subclass of the list object
    """
    def __init__(self):
        """
            bind the params passed
        """
        super().__init__(self)

    def print_sorted(self):
        """
            print the list sorted
        """
        print(sorted(self))
