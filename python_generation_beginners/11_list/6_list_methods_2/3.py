# put your python code here
s = input()
n = 0
s_arr = s.lower().split()
n += s_arr.count('a')
n += s_arr.count('an')
n += s_arr.count('the')

print('Общее количество артиклей: {0}'.format(n))
