#!/usr/bin/python3
"""
    This module  define a  clas Square
"""


from models import rectangle


class Square(rectangle.Rectangle):
    """
    This class represents a square geometric shape
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        square_attr = dict()
        for k, v in self.__dict__.items():
            if k.startswith("_"):
                prefix = "_" + self.__class__.__bases__[0].__name__ + "__"
                k = k[len(prefix):]
                if k == "width" or k == "height":
                    continue
            square_attr[k] = v
        square_attr["size"] = self.width
        return square_attr

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)
