import math


# объявление функции
def get_days(month):
    return 28 + (month + math.floor(month / 8)) % 2 + 2 % month + 2 * math.floor(1 / month)


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
