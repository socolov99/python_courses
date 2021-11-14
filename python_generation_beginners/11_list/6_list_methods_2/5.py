# put your python code here
numbers = [int(x) for x in input().split()]

numbers.sort(reverse=False)
print(*numbers)
numbers.sort(reverse=True)
print(*numbers)
