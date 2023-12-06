#!/usr/bin/python3
"""
Module Disc
"""


def append_write(filename="", text=""):
    """
    Append Func
    """
    with open(filename, 'a', encoding='utf-8') as f:
        nb_characters_added = f.write(text)
        return nb_characters_added
