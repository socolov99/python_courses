# put your python code here
s, k = input(), 0
for i in range(len(s)):
    if s[i].islower():
        k += 1
print(k)
