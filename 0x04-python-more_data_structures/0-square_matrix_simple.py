#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []
    for nums in matrix:
        result.append([i**2 for i in nums])
    return result
