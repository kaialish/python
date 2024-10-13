def SumLine(A, M, N, k):
    if k > M:
        return 0
    return sum(A[k-1])


A = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
]
M = 3
N = 3
k = int(input("Введите номер строки (k): "))

result = SumLine(A, M, N, k)


print(f"Сумма элементов в {k}-й строке: {result}")
