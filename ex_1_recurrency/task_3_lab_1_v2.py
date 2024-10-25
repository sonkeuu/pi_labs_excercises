
import turtle
from turtle import *

turtle.speed(50)
turtle.left(90)
turtle.backward(200)
Screen().tracer(0)

def task_3_lab_1(x, level: int):
    if level == 0:
        return
    else:
        forward(x)
        for i in range(6):
            left(60)
            task_3_lab_1(x/2.7, level - 1)
        left(60)
        right(60)
        back(x)





if __name__ == '__main__':
    #   minimum_x   --->  x / ?
    task_3_lab_1(300, 5)
    turtle.done()