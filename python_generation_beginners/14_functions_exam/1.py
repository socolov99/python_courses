# объявление функции
def draw_triangle():
    i_space = 7
    i_star = 1
    for i in range(8):
        print(i_space * ' ' + i_star * '*')
        i_space -= 1
        i_star += 2


# основная программа
draw_triangle()  # вызов функции
