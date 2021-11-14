# объявление функции
def convert_to_python_case(text):
    sep = '_'
    snake_register = ''
    for i in text:
        if i.isupper():
            snake_register += sep + i.lower()
        else:
            snake_register += i
    return snake_register.lstrip(sep)


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
