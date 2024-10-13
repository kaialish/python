import numpy as np

def stolby_check(matrix):
    matrix_np = np.array(matrix)
    return sum(len(np.unique(matrix_np[:, col])) == matrix_np.shape[0] for col in
               range(matrix_np.shape[1]))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("кол-во столбиков с уник эеленментами", stolby_check(matrix))
