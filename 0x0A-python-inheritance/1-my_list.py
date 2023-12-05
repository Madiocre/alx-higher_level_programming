#!/usr/bin/python3
"""
This Module Prints a List
"""


class MyList(list):
    """
    This class prints a list
    """
    def print_sorted(self):
        self.sort()
        print(self)
