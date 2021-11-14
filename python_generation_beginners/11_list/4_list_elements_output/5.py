# put your python code here
n = int(input())
arr = list()
for i in range(n):
    s = input()
    arr.append(s)

search = input()
for word in arr:
    if search.lower() in word.lower():
        print(word)
