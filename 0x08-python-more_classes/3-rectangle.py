#!/usr/bin/python3
"""
This module is for Rectangle class
"""
class Rectangle:
    """
    This class represents a rectangle with width and height properties.

    Attributes:
       _width (int): The width of the rectangle. It must be an integer and >= 0.
       _height (int): The height of the rectangle. It must be an integer and >= 0.

    Methods:
       __init__: Constructor that initializes the rectangle with optional width and height.
       width: Getter and setter for the width attribute.
       height: Getter and setter for the height attribute.
    """

    def __init__(self, width=0, height=0):
        """
        Constructor that initializes the rectangle with optional width and height.

        Parameters:
           width (int, optional): The width of the rectangle. Defaults to 0.
           height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
           int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Parameters:
           value (int): The new width of the rectangle.

        Raises:
           TypeError: If the value is not an integer.
           ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
        int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.
	Parameters:
           value (int): The new height of the rectangle.

        Raises:
           TypeError: If the value is not an integer.
           ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    def area(self):
        """
        area Function
        """
        return self.__width * self.__height
    def perimeter(self):
        """
        perimeter Function
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
    def __str__(self):
        """
        string format
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join(["#" * self.__width for _ in range(self.__height)])
