def is_prime(num):
    if num == 1:
        return False
    for i in range(2, (num + 1) // 2 + 1):
        if num % i == 0:
            return False
    return True


def is_palindrome(text):
    text_1 = ''
    for i in range(len(text)):
        if text[i] not in '.,!?- ':
            text_1 += text[i]
    text_1 = text_1.lower()
    text_2 = text_1[::-1]
    return text_1 == text_2


# объявление функции
def is_valid_password(password):
    pass_words = password.split(':')
    if len(pass_words) != 3:
        return False
    return is_palindrome(pass_words[0]) and is_prime(int(pass_words[1])) and int(pass_words[2]) % 2 == 0


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
