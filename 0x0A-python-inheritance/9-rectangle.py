#!/usr/bin/python3
"""
Module Disc
"""


class BaseGeometry:
    """
    Class to raise Exception
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rect Class disc
    """
    def __init__(self, width, height):
        """
        init
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        str format
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        area Function
        """
        return self.__width * self.__height
