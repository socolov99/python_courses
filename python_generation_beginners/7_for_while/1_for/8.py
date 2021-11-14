# put your python code here
m = int(input())
p = int(input())
n = int(input())
for i in range(0, n):
    print(i + 1, m)
    m += m * p / 100
