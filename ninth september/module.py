def lool(X, Y, Z):

    if X >= Y >= Z:
        X, Y, Z = 2 * X, 2 * Y, 2 * Z
    else:
       X, Y, Z = -X, -Y, -Z
    return X, Y, Z


