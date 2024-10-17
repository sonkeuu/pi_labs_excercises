import turtle
from turtle import *


def task_a1(x, minimum_x):
    if x < minimum_x:
        return
    for i in range(4):
        forward(x)
        left(180)
        task_a1(x/2, minimum_x)
        left(90)


def task_1_lab_1(x, minimum_x):
    if x < minimum_x:
        return
    for i in range(4):
        forward(x)
        left(90)
        task_1_lab_1(x/3, minimum_x)


def task_2_lab_1(x, minimum_x):
    if x < minimum_x:
        return
    for i in range(4):
        forward(x)
        left(180)
        forward(3*x/4)
        left(270)
        task_2_lab_1(x/2, minimum_x)
        #   right(90)


def task_3_lab_1(x, minimum_x):
    if x < minimum_x:
        return
    for i in range(4):
        forward(x)
        left(180)
        task_3_lab_1(x/4, minimum_x)
        forward(x)
        left(90)


if __name__ == '__main__':

    #   Task_A1(300).shape_inside()

    #   task_1_lab_1(270, 10)
    task_2_lab_1(256, 128)
    turtle.done()