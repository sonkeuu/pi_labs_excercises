import turtle
from turtle import *

turtle.speed(50)
Screen().tracer(0)


def task_a1(x, level):
    if level == 0:
        return
    for i in range(4):
        forward(x)
        left(180)
        task_a1(x/2, level - 1)
        left(90)


if __name__ == '__main__':

    #   minimum_x   --->  x / 9
    task_a1(100, 4)
    turtle.done()