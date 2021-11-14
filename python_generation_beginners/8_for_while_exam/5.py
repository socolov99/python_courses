# put your python code here
n = int(input())
while n > 999:
    n //= 10
print(n % 10)
