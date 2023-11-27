#!/usr/bin/python3
"""
This module provides a Square class that represents a square.

The Square class has a private attribute '__size' that represents the size of the square.
It has methods to get and set the size of the square.
"""

class Square:
    """
    A class representing a square.                                                                                                                                                   
    Attributes:
    __size (int): The size of the square.
    """
    def __init__(self, size):
        """                                                                                                                                                                        
        The constructor for Square class.
        Args:
        size (int): The size of the square.
        """
        self.__size = size

