import turtle
from turtle import *

turtle.speed(15)

def task_2_lab_1(x, minimum_x):
    if x < minimum_x:
        return
    for i in range(4):
        forward(x)
        left(90)
        forward(x)
        left(180)
        task_2_lab_1(x/1.5, minimum_x)



if __name__ == '__main__':

    #   minimum_x   --->  x / 16
    task_2_lab_1(256, 128)
    turtle.done()