import numpy as np
def count_unique_stolby(matrix):
    np_matrix = np.array(matrix)
    check_stolby = 0

    for column in np_matrix.T:
        if len(np.unique(column)) == len(column):
            check_stolby += 1

    return check_stolby


