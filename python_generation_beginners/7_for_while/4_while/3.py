# put your python code here
a, k = input(), 0
while a not in ('стоп', 'хватит', 'достаточно'):
    k += 1
    a = input()
print(k)
