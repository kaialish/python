def list_of_numbers (cypfri):
    min_num = float('inf')
    max_num = float('-inf')
    min_i = -1
    max_i = -1

    for i, num in enumerate(cypfri):
        if num < min_num:
            min_num = num
            min_i = i
        if num > max_num:
            max_num = num
            max_i = i

    if min_i < max_i:
        return min_i
    else:
        return max_i


ura_cyfri = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
i = list_of_numbers(ura_cyfri)
print("Номер первого экстремального элемента", i)
