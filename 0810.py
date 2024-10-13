import random

def Norm1(A, M, N):
    max_sum = 0
    for j in range(N):
        column_sum = 0
        for i in range(M):
            column_sum += abs(A[i][j])
        if column_sum > max_sum:
            max_sum = column_sum
    return max_sum


M = 5
N = 3
A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(M)]

print("Матрица A:")
for row in A:
    print(row)

print("Norm1(A, M, N):", Norm1(A, M, N))


