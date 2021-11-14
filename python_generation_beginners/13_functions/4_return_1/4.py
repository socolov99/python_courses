# объявление функции
def get_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


# объявление функции
def number_of_factors(num):
    return len(get_factors(num))


# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
