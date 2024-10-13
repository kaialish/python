import math

def calculator(dano, okruzhnost):
    pi = 3.14
    if okruzhnost == 1:
        R = dano
        D = 2 * R
        L = 2 * pi * R
        S = pi * R ** 2
    elif okruzhnost == 2:
        D = dano
        R = D / 2
        L = pi * D
        S = pi * (R ** 2)
    elif okruzhnost == 3:
        L = dano
        R = L / (2 * pi)
        D = 2 * R
        S = pi * (R ** 2)
    elif okruzhnost == 4:
        S = dano
        R = math.sqrt(S / pi)
        D = 2 * R
        L = 2 * pi * R
    else:
        return "Неверный номер элемента"

    return R, D, L, S



element_number = 3 #радиус 1, диаметр 2, длина 3, площадь 4
value = 410  #значение

R, D, L, S = calculator(value, element_number)
print("Радиус (R):", R)
print("Диаметр (D):", D)
print("Длина окружности (L):", L)
print("Площадь круга (S):", S)
