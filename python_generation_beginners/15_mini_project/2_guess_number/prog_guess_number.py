from random import randint


def is_valid(s):
    global rn
    try:
        return 1 <= int(s) <= rn
    except ValueError:
        return False


def play(rn):
    n = randint(1, rn)
    x = 0
    count = 0
    is_playing = True
    print('Угадайте число от 1 до {}'.format(rn))
    while is_playing:
        x = input()
        if not is_valid(x):
            print('А может быть все-таки введем целое число от 1 до {}?'.format(rn))
        else:
            count += 1
            x = int(x)
            if x < n:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif x > n:
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!', 'Было затрачено {} попыток'.format(count), sep='\n')

                is_playing = False
    print('Сыграть еще раз ?\nВведите "Да" если хотите сыграть еще раз\nЕсли хотите закончить введите любой другой символ')
    if input() == 'Да':
        play(rn)


print('Добро пожаловать в числовую угадайку')
print('Выберите праву границу игры')
rn = int(input())

play(rn)

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
