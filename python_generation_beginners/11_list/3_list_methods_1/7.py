# put your python code here
n = int(input())
arr = []
for i in range(n):
    b = int(input())
    arr.append(b)

del arr[1::2]
print(arr)
