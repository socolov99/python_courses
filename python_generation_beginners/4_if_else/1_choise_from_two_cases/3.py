# put your python code here
n = int(input())
a1 = n // 1000
a4 = n % 10
a2 = n // 100
a2 %= 10
a3 = n // 10
a3 %= 10
if a1 + a4 == a2 - a3:
    print('ДА')
else:
    print('НЕТ')
