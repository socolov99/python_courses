# объявление функции
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, (num + 1) // 2 + 1):
        if num % i == 0:
            return False
    return True


# объявление функции
def get_next_prime(num):
    num += 1
    if is_prime(num):
        return num
    else:
        return get_next_prime(num)


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
