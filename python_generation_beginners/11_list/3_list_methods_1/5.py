# put your python code here
n = int(input())
ls = []
for i in range(1, n + 1):
    if n % i == 0:
        ls.append(i)
print(ls)
