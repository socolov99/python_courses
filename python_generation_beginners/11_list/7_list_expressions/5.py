# put your python code here
n = int(input())
print(*[(i + 1) ** 2 for i in range(n)], sep='\n')
