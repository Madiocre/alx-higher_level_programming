#!/usr/bin/python3
"""
Module Disc
"""
def read_file(filename=""):
    """
    Func to read
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
