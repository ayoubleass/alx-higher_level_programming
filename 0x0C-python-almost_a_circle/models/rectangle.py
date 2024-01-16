#!/usr/bin/python3
"""
    This module define a class Rectangle.
"""


from models import base


class Rectangle(base.Base):
    """
    This class represents a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.
        """
        self.validate("width", width)
        self.validate("height", height)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate("width", value)
        self.__width = value

    @property
    def height(height):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate('x', value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate('y', value)
        self.__y = value

    def area(self):
        """
        Return the area of a rectangle
        """
        return self.__width * self.__height

    def display(self):
        for n in range(self.__y):
            print('')
        for num in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x,
                self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        rect_att = dict()
        for k, v in self.__dict__.items():
            if k.startswith("_"):
                prefix = "_" + self.__class__.__name__ + "__"
                k = k[len(prefix):]
            rect_att[k] = v
        return rect_att

    def validate(self, name, value):
        """
        Check if the binding is done correctly
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{}  must be >= 0".format(name))
