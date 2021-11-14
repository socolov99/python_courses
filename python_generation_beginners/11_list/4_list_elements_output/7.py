# put your python code here
n = int(input())
l1 = []
l2 = []
l3 = []

for i in range(n):
    s = int(input())
    if s < 0:
        l1.append(s)
    elif s == 0:
        l2.append(s)
    else:
        l3.append(s)
for digit in l1:
    print(digit)
for digit in l2:
    print(digit)
for digit in l3:
    print(digit)
