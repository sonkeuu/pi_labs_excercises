import turtle
from turtle import *

turtle.speed(50)
#Screen().tracer(0)


def task_2_lab_1(x, minimum_x):
    if x < minimum_x:
        return
    else:
        for i in range(4):
            for j in range(4):
                forward(x)
                left(90)
            forward(x/4)
            right(90)
            task_2_lab_1(x / 2, minimum_x)


def shape2(x, minx):
    if x < minx:
        return
    else:
        for i in range(2):
            right(90)
            forward((4/3) * x)
            left(90)
            forward(x/3)
            shape(x/2, minx)
            forward(x)
            left(180)


def shape(x, lvl):
    if lvl == 0:
        return
    else:
        for i in range(2):
            forward(x)
            right(90)
            forward(3*x/4)
            left(180)
            shape(x/2, lvl - 1)
            left(180)
            forward(x/4)
            right(90)


if __name__ == '__main__':

    #   minimum_x   --->  x / 16
    #test(100, 10)
    #task_2_lab_1(200, 25)
    #left(90)
    shape(200, 4)
    turtle.done()