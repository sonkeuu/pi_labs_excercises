import turtle
from turtle import *

turtle.speed(0)
#Screen().tracer(0)


def task_1_lab_1(x, level):
    if level == 0:
        return
    for i in range(4):
        forward(x)
        left(90)
        task_1_lab_1(x / 3, level - 1)


if __name__ == '__main__':

    #   minimum_x   --->  x / 27
    task_1_lab_1(270, 4)
    turtle.done()
