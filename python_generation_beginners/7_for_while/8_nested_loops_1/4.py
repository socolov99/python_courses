# put your python code here
n = int(input())
for i in range(1, n + 1):
    print('*' * min(i, n - i + 1))
