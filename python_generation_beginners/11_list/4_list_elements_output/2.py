# put your python code here
numbers = []
y = []
n = int(input())
for x in range(n):
    val = int(input())
    numbers.append(val)
    y.append(val ** 2 + 2 * val + 1)

print(*numbers, sep='\n')
print()
print(*y, sep='\n')
