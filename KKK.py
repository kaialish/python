def pervoe_cheslo(K):
    plus1 = 1
    while True:
        num = int(input("Введите любое число: "))
        if num == 0:
            return 0
        if num > K:
            return plus1
        plus1 += 1


