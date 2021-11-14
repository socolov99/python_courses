# put your python code here
s = input()
number_of_strings = int(s[1:])
code_str = list()
for i in range(number_of_strings):
    x = input()
    if '#' in x:
        code_str.append(x[:x.index('#')].rstrip())
    else:
        code_str.append(x.rstrip())

for x in code_str:
    print(x)
