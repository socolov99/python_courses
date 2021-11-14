# put your python code here
n = int(input())
arr = list()

for i in range(n):
    s = input()
    arr.append(s)

arr_k = list()
k = int(input())
for i in range(k):
    s = input()
    arr_k.append(s)

for word in arr:
    flag = True
    for k in arr_k:
        if k.lower() not in word.lower():
            flag = False
    if flag:
        print(word)
