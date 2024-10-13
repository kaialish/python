def summi(number):
    return sum(int(digit) for digit in str(number))

def naidy_happy():
    happy = []
    for number in range(100000, 1000000):

        first_half = number // 1000
        second_half = number % 1000


        if summi(first_half) == summi(second_half):
            happy.append(number)
    return happy
happy_numbers = naidy_happy()
print(happy_numbers)
