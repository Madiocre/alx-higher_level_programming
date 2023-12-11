#!/usr/bin/python3
from models.base import Base
"""
Module Disc
"""


class Rectangle(Base):
    """
    Base Class Disc
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__ Disc
        """
        super().__init__(id)
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
   
        self.__width = width
        self.__height = height
   
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
   
        self.__x = x
   
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
   
        self.__y = y
        
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        return self.__width * self.__height

    def display(self):
        """
        To handle width and height, x and y
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
    
    def update(self, *args):
        """
        Updates depending on input
        """
        self.id = args[0] if args else self.id
        self.__width = args[1] if len(args) > 1 else self.__width
        self.__height = args[2] if len(args) > 2 else self.__height
        self.__x = args[3] if len(args) > 3 else self.__x
        self.__y = args[4] if len(args) > 4 else self.__y
