#!/usr/bin/python3
import unittest
from models import base,rectangle,square


class TestBase(unittest.TestCase):
    def test_base(self):
        try:
            b = base.Base()
            self.assertTrue(True)
        except ImportError:
            self.fail("Module not found")

    def test_rectangle(self):
        r = rectangle.Rectangle(10,5)
        self.assertEqual(r.id, 2)

    def test_rectangle_validate(self):
        try: 
            r = rectangle.Rectangle(10,'5', 1, 2, 5)
            self.fail("height must be an integer")
        except TypeError as e:
            self.assertEqual(str(e), "height must be an integer")

    def test_rectangle_area(self):
        r = rectangle.Rectangle(3,2)
        self.assertEqual(r.area(), 6)

    def test_square(self):
        s = square.Square(5)
        if isinstance(s, rectangle.Rectangle):
            self.assertTrue(True)
        else:
            raise Exception("{} not an instance of Rectangle".fromat(r))

    def test_sqaure_binding(self):
        s = square.Square(5)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.size, 10)
