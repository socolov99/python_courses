# put your python code here
n = int(input())

n1 = n
a = n1 % 10
n1 //= 10
b = n1 % 10
n1 //= 10
c = n1

print('Сумма цифр =', a + b + c)
print('Произведение цифр =', a * b * c)
