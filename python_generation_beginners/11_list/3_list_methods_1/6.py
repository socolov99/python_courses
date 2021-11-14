# put your python code here
n, a, c = int(input()), int(input()), []
for i in range(n - 1):
    b = int(input())
    c.append(a + b)
    a = b
print(c)
