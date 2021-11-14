# put your python code here
numbers = []
n = int(input())
for x in range(n):
    val = int(input())
    numbers.append(val)

del numbers[numbers.index(min(numbers))]
del numbers[numbers.index(max(numbers))]

print(*numbers, sep='\n')
