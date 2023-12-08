#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    placeholder = []
    for row in matrix:
        for i in range(0, len(row)):
            placeholder.append(row[i] * row[i])
            if i == len(row) - 1:
                square.append(placeholder)
                placeholder = []
    return square
