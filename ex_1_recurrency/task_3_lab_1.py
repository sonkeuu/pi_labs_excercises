import turtle
from turtle import *

turtle.speed(50)
turtle.left(90)

def task_3_lab_1(x, minimum_x):
    if x < minimum_x:
        return
    else:
        forward(x*2)
        for i in range(6):
            forward(x)
            task_3_lab_1(x/2.7, minimum_x)
            backward(x)
            right(60)
        backward(2*x)


if __name__ == '__main__':
    #   minimum_x   --->  x / ?
    task_3_lab_1(100, 5)
    turtle.done()