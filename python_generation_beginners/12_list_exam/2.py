# put your python code here
lst_1 = [int(i) for i in input().split()]
lst_2 = [int(i) for i in input().split()]

print(*[lst_1[i] + lst_2[i] for i in range(len(lst_1))])
