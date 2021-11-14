# put your python code here

w, n = [input() for i in range(int(input()))], int(input())
print(''.join((i[n - 1] for i in w if 1 <= n <= len(i))))
