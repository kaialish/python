def DecToBin(N):
    if N == 0:
        return "0"
    binary = ""
    while N > 0:
        binary = str(N % 2) + binary
        N = N // 2
    return binary


N = int(input("Введите число не меньше нуля: "))
print(f"Двоичное представление числа {N}: {DecToBin(N)}")
