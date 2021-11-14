# put your python code here

s = input()
d = ''
for i in range(0, len(s)):
    if i % 3 != 0:
        d += s[i]
print(d)
