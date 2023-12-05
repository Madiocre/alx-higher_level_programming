#!/usr/bin/python3
"""
This Module Prints a List
"""


class MyList(list):
    """
    This class prints a list
    """
    def print_sorted(self):
        copy_list = self[:]
        copy_list.sort()
        print(copy_list)
