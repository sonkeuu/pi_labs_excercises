import turtle
from turtle import *

turtle.speed(15)


def task_a1(x, minimum_x):
    if x < minimum_x:
        return
    for i in range(4):
        forward(x)
        left(180)
        task_a1(x/2, minimum_x)
        left(90)


if __name__ == '__main__':

    #   minimum_x   --->  x / 9
    task_a1(270, 30)
    turtle.done()