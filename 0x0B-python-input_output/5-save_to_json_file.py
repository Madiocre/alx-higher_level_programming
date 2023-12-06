#!/usr/bin/python3
"""
Module Disc
"""


def save_to_json_file(my_obj, filename):
    """
    JSON save
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
