#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Module Disc
"""


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
