# put your python code here
s = input()
c = s.count('f')

if c == 0:
    print(-2)
elif c == 1:
    print(-1)
else:
    print(s.find('f', s.find('f') + 1))
