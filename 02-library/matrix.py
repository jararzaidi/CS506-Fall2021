from functools import reduce

def get_determinant(matrix):
    negative = 0
    postive =0
    fold_matrix = (lambda x, y: x * y)

    
    for x in range(len(matrix)):
        
        postive = postive +  reduce(fold_matrix, [matrix[(x+val)%len(matrix)][val] for val in range(len(matrix))])
        
    
    for y in range(len(matrix)):
          negative = negative + reduce(fold_matrix, [matrix[(len(matrix)-y-val)%len(matrix)][val] for val in range(len(matrix))])
    return (postive - negative)

matrix1 = [[1, 0, 2, -1],
         [3, 0, 0, 5],
         [2, 1, 4, -3],
         [1, 0, 5, 0]]
matrix2 = [[0,0,0,0]]
matrix3 = [[9,4,1,0,5]]
print(get_determinant(matrix1))
print(get_determinant(matrix2))
print(get_determinant(matrix3))