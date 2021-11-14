# объявление функции
def find_all(target, symbol):
    x = []
    for i in range(len(target)):
        if target[i] == symbol:
            x.append(i)
    return x


# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
