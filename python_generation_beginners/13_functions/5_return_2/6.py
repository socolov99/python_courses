# объявление функции
def is_palindrome(text):
    text_1 = ''
    for i in range(len(text)):
        if text[i] not in '.,!?- ':
            text_1 += text[i]
    text_1 = text_1.lower()
    text_2 = text_1[::-1]
    return text_1 == text_2


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
