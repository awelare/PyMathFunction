from turtle import *
from math import *
step = 50 #размер клетки 1кл = 1 ед

def draw_grid(t, step, width, height):#тут рисуем сетку
    t.speed(0)
    t.color("lightgray")
    t.hideturtle()
    for x in range(-width//2, width//2+1, step):
        t.penup()
        t.goto(x, -height//2)
        t.pendown()
        t.goto(x, height//2)
    for y in range(-height//2, height//2+1, step):
        t.penup()
        t.goto(-width//2, y)
        t.pendown()
        t.goto(width//2, y)
def draw_axes(t, width, height):#тут рисуем оси
    t.speed(0)
    t.color("black")
    t.hideturtle()
    t.penup()
    t.goto(0, -height//2)
    t.pendown()
    t.goto(0, height//2)
    t.penup()
    t.goto(-width//2, 0)
    t.pendown()
    t.goto(width//2, 0)
screen = Screen()
screen.setup(800, 600)
screen.tracer(0)#скип анимаций
t=Turtle()
draw_grid(t, step, 800, 600)
draw_axes(t, 800, 600)
screen.update()

drawer = Turtle()
drawer.hideturtle()
drawer.color("red")

formula = screen.textinput("График функций", "Введите формулу f(x) в формате:(без {}) {x*sin(x)}, список доступных функций:\n"
                                             "+, -, /, * - сложить, вычесть, разделить, умножить\n"
                                             "sin(x), cos(x), tan(x) - синус, косинус, тангенс\n"
                                             "asin(x), acos(x), atan(x) - обратные тригонометрические функции(аркусы)\n"
                                             "sqrt(x) - квадратный корень\n"
                                             "pow(x,y) или x**y - x^y\n"
                                             "abs(x) - модуль числа\n"
                                             "cell(x) - округление до ближайшего целого вверх floor(x) - округление до ближайшего целого вниз \n"
                                             "pi - 3.14159....")
if formula:
    drawer.penup()
    drawer.pensize(2)
    for x_p in range(-400, 401):
        x = x_p/step
        try:
            y_m = eval(formula)
            y_p = y_m*step
            if x_p == -400:
                drawer.goto(x_p, y_p)
                drawer.pendown()
            else:
                drawer.goto(x_p, y_p)
        except:
            drawer.penup()
            continue

screen.update()
t.speed(0)
exitonclick()
