# put your python code here
n, roman_numbers = int(input()), ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
print(roman_numbers[n - 1] if 1 <= n <= 10 else 'ошибка')
