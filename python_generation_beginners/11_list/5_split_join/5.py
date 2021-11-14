# put your python code here
s = input()

flag = True
for word in s.split('.'):
    if not 0 <= int(word) <= 255:
        flag = False

if flag:
    print('ДА')
else:
    print('НЕТ')
