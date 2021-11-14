lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']


# объявление функции
def get_month(language, number):
    switch = {
        'ru': lng_ru[number - 1],
        'en': lng_en[number - 1]
    }
    return switch[language]


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
