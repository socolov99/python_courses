# объявление функции
def is_magic(date):
    data = date.split('.')
    return int(data[0]) * int(data[1]) == int(data[2]) % 100


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
