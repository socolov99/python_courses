# объявление функции
def print_fio(name, surname, patronymic):
    print(surname[0].capitalize(), end='')
    print(name[0].capitalize(), end='')

    print(patronymic[0].capitalize(), end='')


# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)
