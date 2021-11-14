# put your python code here
n = int(input())

n1 = n
c = n1 % 10
n1 //= 10
b = n1 % 10
n1 //= 10
a = n1

print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')
