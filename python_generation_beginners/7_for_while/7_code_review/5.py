# put your python code here
n = int(input())
while n > 9:  # Ошибка - цикл имеет смысл только в случае если данное натурально число дву- и  более -значное.
    n //= 10  # Ошибка - нам необходимо постепенно отбрасывать числа до первого, а не выяснять последние из них.
print(n)