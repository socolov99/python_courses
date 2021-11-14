# put your python code here
n = int(input())
arr = list()
for i in range(n):
    s = input()
    if s not in arr:
        arr.append(s)
        print(s)
