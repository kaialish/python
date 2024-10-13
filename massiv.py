def massiv_right(spisok):
    last_ele = spisok[-1]
    for i in range(len(spisok) - 1, 0, -1):
        spisok[i] = spisok[i - 1]
    spisok[0] = last_ele
    return spisok



