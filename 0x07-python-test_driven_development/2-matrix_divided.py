#!/usr/bin/python3
"""
This Module Divides Matrix by Num
"""
def matrix_divided(matrix, div):
    """
    Method to divide all matrix vals by a num

    Args:
    matrix: list to print
    div: number to divide by

    Raises:
    ZeroDivisionError: 
    TypeError:
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if(div == 0):
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    result = [[round(i/div, 2) for i in row] for row in matrix]
    return result

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
