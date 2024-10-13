def check(number):
    a1 = number // 1000
    a2 = (number // 100) % 10
    a3 = (number // 10) % 10
    a4 = number % 10

    if (a1 + a2) == (a3 + a4):
        return "Истина"
    else:
        return "ЛОООООЖЖь"
