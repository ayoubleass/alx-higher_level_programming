#!/usr/bin/python3
"""
    This module define a class student
"""


class Student:
    """
        This class reperesent a student 
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializing  the instance attribute
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
