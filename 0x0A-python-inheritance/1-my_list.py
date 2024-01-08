#!/usr/bin/python3
"""
    This module conntaine a subclass of the list class
"""


class MyList(list):
    """
        This class is a subclass of the list object
    """
    def print_sorted(self):
        """
            print the list sorted
        """
        print(sorted(self))
