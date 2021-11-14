# put your python code here
def draw_triangle(fill, base):
    for i in range(base // 2 + 2):
        print(fill * i)
    for j in range(base // 2, 0, -1):
        print(fill * j)


fill, base = input(), int(input())
draw_triangle(fill, base)
