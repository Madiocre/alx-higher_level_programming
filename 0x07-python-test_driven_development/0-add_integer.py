#!/usr/bin/python3
"""
This Module Adds two integers or casted floats
"""
def add_integer(a, b=98):
    """
    Method to add Two Integers or Floats

    Args:
    a: First Int or Float
    b: Second Int or Float, Default 98

    Raises:
    TypeError: If a or b is not an Int or Float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    c = int(a) + int(b)
    return c

if __name__ == "__main__":
    import doctest
    doctest.testfile("/tests/0-add_integer.txt")
