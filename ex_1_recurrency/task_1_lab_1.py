import turtle
from turtle import *

turtle.speed(50)


def task_1_lab_1(x, minimum_x):
    if x < minimum_x:
        return
    for i in range(4):
        forward(x)
        left(90)
        task_1_lab_1(x / 3, minimum_x)


if __name__ == '__main__':

    #   minimum_x   --->  x / 27
    task_1_lab_1(270, 10)
    turtle.done()
