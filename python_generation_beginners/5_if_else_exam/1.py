# put your python code here
a = int(input())

last_num = a % 10
second_num = a // 10 % 10
if last_num == second_num == 0:
    print('YES')
else:
    print('NO')
