#!/usr/bin/python3
"""
Module Disc
"""


def read_file(filename=""):
    """
    Func to read
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
