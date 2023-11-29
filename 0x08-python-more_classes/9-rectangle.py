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
    number_of_instances = 0
    print_symbol = '#'
    
    def __init__(self, width=0, height=0):
        """
        Constructor that initializes the rectangle with optional width and height.

        Parameters:
           width (int, optional): The width of the rectangle. Defaults to 0.
           height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
    def __del__(self):
        """
        Deconstructor that handles the Deletion of rectangle
        """
        print ("Bye rectangle...")
        Rectangle.number_of_instances -= 1
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
        str Handler
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join([Rectangle.print_symbol * self.__width for _ in range(self.__height)])
    def __repr__(self) -> str:
        """
        repr Handler
        """
        return f"Rectangle({self._width}, {self._height})"
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        bigger_or_equal static method
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
    @classmethod
    def square(cls, size=0):
        """
        Create a Separate Square
        """
        Square = Rectangle(size,size)
        return Square
