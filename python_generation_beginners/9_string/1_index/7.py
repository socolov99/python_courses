# put your python code here
n = input()
s = 'Цифр нет'
for i in range(len(str(n))):
    if n[i] in '0123456789':
        s = 'Цифра'
print(s)
