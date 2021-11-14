# put your python code here
n, s = int(input()), input()
for c in s:
    if ord(c) - n < 97:
        print(chr(122 - (96 - ord(c) + n)), end='')
    else:
        print(chr(ord(c) - n), end='')
