# put your python code here
lst = [int(i) for i in input().split()]
print(*[x for x in lst], sep='+', end='=')
print(sum(lst))
