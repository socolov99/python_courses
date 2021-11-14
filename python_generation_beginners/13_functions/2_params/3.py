# объявление функции
def print_digit_sum(num):
    summ = 0
    s = str(num)
    for x in s:
        summ += int(x)
    print(summ)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
