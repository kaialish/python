import re
def is_sentence_palindrome(sentence):
    # space = ''.join(sentence.lower().split())
    # a = re.sub(r'[^\w]','', polzovatel)
    space = re.sub(r'[^\w]', '', sentence.lower())
    return space == space[::-1]
    # return space == space[::-1]
polzovatel = input("Введите строку: ")
if is_sentence_palindrome(polzovatel):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")
