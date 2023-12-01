#!/usr/bin/python3
"""
This Madule Says My Name
"""
def say_my_name(first_name, last_name=""):
    """
    Method to divide all matrix vals by a num

    Args:
    first_name: first
    last_name: last

    Raises:
    TypeError:
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("/tests/3-say_my_name.txt")
