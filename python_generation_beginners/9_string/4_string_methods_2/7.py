# put your python code here
s = input()

if s.count('f') == 0:
    print('NO')
elif s.count('f') == 1:
    print(s.find('f'))
else:
    print(s.find('f'), s.rfind('f'))
