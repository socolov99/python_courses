# put your python code here
s = input()
i1 = s.find('h')
l2 = s.rfind('h')
a = s[:i1]
b = s[s.find('h'):l2 + 1]
c = s[l2 + 1:]
s = a + b[::-1] + c
print(s)
