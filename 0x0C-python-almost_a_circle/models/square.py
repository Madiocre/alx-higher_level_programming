#!/usr/bin/python3
from models.rectangle import Rectangle
"""
Module Disc
"""


class Square(Rectangle):    
    """
    Base Class Disc
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size

    @property
    def size(self):
        """
        Size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        
        self.__size = value

    def __str__(self):
        """
        STR format
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__size}"
    
    def update(self, *args, **kwargs):
        """
        Update
        """
        if args and len(args) > 0:
            self.id = args[0]
            self.width = args[1]
            self.height = args[1]
            self.x = args[2]
            self.y = args[3]
        else:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """
        Dict
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }