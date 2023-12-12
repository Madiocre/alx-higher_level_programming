#!/usr/bin/python3
from models.base import Base
"""
Module Disc of a RECTANGLE
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
        
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        
        self.__width = width
        
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        
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
        """
        Width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        X
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        X
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        """
        Area
        """
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
        """
        STR format
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
    
    def update(self, *args, **kwargs):
        """
        Update depending on input
        """
        if args and len(args) > 0:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        else:
            self.id = kwargs.get('id', self.id)
            self.__width = kwargs.get('width', self.__width)
            self.__height = kwargs.get('height', self.__height)
            self.__x = kwargs.get('x', self.__x)
            self.__y = kwargs.get('y', self.__y)

    def to_dictionary(self):
        """
        dict
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
