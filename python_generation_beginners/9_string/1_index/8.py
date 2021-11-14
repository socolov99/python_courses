# put your python code here
a = input()
star = 0
plus = 0
for i in a:
    if i == '*':
        star += 1
    elif i == '+':
        plus += 1
print('Символ + встречается', plus, 'раз')
print('Символ * встречается', star, 'раз')
