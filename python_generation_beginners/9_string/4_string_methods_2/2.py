# put your python code here
s = input()
a = 0
g = 0
c = 0
t = 0
lower_s = s.lower()
a = lower_s.count('а')
g = lower_s.count('г')
c = lower_s.count('ц')
t = lower_s.count('т')
print('Аденин:', a)
print('Гуанин:', g)
print('Цитозин:', c)
print('Тимин:', t)
