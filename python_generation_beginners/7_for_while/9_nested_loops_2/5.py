# put your python code here
n = int(input())
while n // 10 > 0:
    n = n // 10 + n % 10
print(n)
