
import turtle
from turtle import *

turtle.speed(50)


def task_1_lab_1(x, minimum_x):
    if x < minimum_x:
        return
    for i in range(2):
        forward(x)
        right(90)
        forward(x)
        right(90)
        task_1_lab_1(x / 2, minimum_x)


if __name__ == '__main__':

    #   minimum_x   --->  x / 27
    task_1_lab_1(200, 10)
    turtle.done()
