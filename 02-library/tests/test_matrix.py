import pytest

def main(matrix):
    matrix1 = [[1, 0, 2, -1],
         [3, 0, 0, 5],
         [2, 1, 4, -3],
         [1, 0, 5, 0]]
    matrix2 = [[0,0,0,0]]
    matrix3 = [[9,4,1,0,5]]
    print(get_determinant(matrix1))
    print(get_determinant(matrix2))
    print(get_determinant(matrix3))
