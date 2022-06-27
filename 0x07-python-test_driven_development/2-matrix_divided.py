#!/usr/bin/python3
"""
This Module has a function that divides all elements of a matrix.
   Prototype: def matrix_divided(matrix, div):
"""


def matrix_divided(matrix, div):
    """Returns a new matrix

    Args: 
        matrix (list of lists of integers/floats): The matrix.
        div (number(int or float)): Number to use to divide every element.
    """

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if not is_conformed_matrix(matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    if not elements_have_same_size(matrix):
        raise TypeError('Each row of the matrix must have the same size')
        
    m = list(map(lambda x: list(map(lambda y: round(y/div, 2), x)), matrix))

    return m

def is_conformed_matrix(matrix):
    """Helper function that check if the matrix is a list of lists
    of integers/floats"""

    is_conformed = False

    if type(matrix) is not list:
        return is_conformed

    if len(matrix) == 0:
        return is_conformed

    """verify if every sublist of matrix:
        # has the type list
        # has the same size
        and if elements of sublist are integers or floats numbers
    """

    for i in range(len(matrix)):

        if type(matrix[i]) is not list:
            return is_conformed

        for element in matrix[i]:
            if type(element) not in [int, float]:
                return is_conformed

    is_conformed = True
    
    return is_conformed

def elements_have_same_size(matrix):
    """Helper function that checks if every
    sublist of the matrix has the size."""

    first_sublist_size = len(matrix[0])

    for i in range(1, len(matrix)):
        if first_sublist_size != len(matrix[i]):
            return False

    return True
