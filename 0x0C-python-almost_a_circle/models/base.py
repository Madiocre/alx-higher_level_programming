#!/usr/bin/python3
"""
Module Disc
"""


class Base:
    """
    Base Class Disc
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        __init__ Disc
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects