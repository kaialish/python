def exp1(x, eps):
    term = 1  #слагаемое
    sum = term  #начальная сумма
    n = 1  #факториал

    while abs(term) > eps:
        term *= x / n  #слагаемое
        sum += term  #добавляем его к сумме
        n += 1  #+1 факториал

    return sum


x = 2.0
eps_values = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001]

for eps in eps_values:
    print(f"Exp1({x}, {eps}) = {exp1(x, eps)}")
