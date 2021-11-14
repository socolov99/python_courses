# put your python code here
s = input().lower()
print('Количество гласных букв равно', sum(1 for _ in s if _ in 'ауоыиэяюёе'))
print('Количество согласных букв равно', sum(1 for _ in s if _ in 'бвгджзйклмнпрстфхцчшщ'))
