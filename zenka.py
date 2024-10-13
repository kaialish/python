letter_to_gpa = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
gpa_to_letter = {4.0: 'A', 3.0: 'B', 2.0: 'C', 1.0: 'D', 0.0: 'F'}
while True:
    value = input("Введите оценку: ")
    if value == "":
        break
    try:
        num_value = float(value)
        if num_value in gpa_to_letter:
            print("Буквенная оценка:", gpa_to_letter[num_value])
        else:
            print("Недопустимая числовая оценка")
    except ValueError:

        if value in letter_to_gpa:
            print("Оценка в GPA:", letter_to_gpa[value])
        else:
            print("Недопустимая буквенная оценка")
