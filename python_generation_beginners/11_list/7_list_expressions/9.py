# put your python code here
print(*[int(n) ** 2 for n in input().split() if (int(n) ** 2) % 10 != 4 and int(n) % 2 == 0])
