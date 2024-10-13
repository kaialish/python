A = float(input("Введите число A (> 1): "))
N = 1
seria_sum = 1.0

while seria_sum + 1 / (N + 1) < A:
    N += 1
    seria_sum += 1 / N

seria_sum = round(seria_sum, 1)
print("Наибольшее целое число N: ", N)
print("Сумма ряда: ",  seria_sum)
