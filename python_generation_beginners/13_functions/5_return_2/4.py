# объявление функции
def is_password_good(txt):
    if len(txt) < 8 or txt.isupper() or txt.islower() or txt.isalpha() or txt.isdigit():
        return False
    for ch in txt:
        if ch in '0123456789':
            return True
    return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
