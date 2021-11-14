# put your python code here
s = input()
symb = s[0]
max = s.count(s[0])
for i in range(1, len(s)):
    if s.count(s[i]) >= max:
        max = s.count(s[i])
        symb = s[i]
print(symb)
