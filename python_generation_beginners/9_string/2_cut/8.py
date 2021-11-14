# put your python code here
s = input()
x = len(s)
a = x // 2 + x % 2
print(s[a:] + s[:a])
