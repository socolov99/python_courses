# put your python code here
p = 0
n = int(input())
for i in range(n):
    for j in range(i + 1):
        print(p + 1, end=' ')
        p += 1
    print()
