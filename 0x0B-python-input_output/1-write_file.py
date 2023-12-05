#!/usr/bin/python3
"""
Module Disc
"""
def write_file(filename="", text=""):
    """
    Func for write
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return len(text)
