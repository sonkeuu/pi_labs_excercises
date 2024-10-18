import turtle
from turtle import *

turtle.speed(2)

def task_2_lab_1(x, minimum_x):
    if x < minimum_x:
        return
    for i in range(4):
        for j in range(4):
            forward(x)
            left(90)
        forward(x/4)
        right(90)
        task_2_lab_1(x / 2, minimum_x)



def test(x, minx):
    if x< minx:
        return
    for i in range(4):
        for j in range(6):
            forward(x)
            left(90)
        forward(x/4)
        right(90)
        test(x/2, minx)
    test(x, minx)




if __name__ == '__main__':

    #   minimum_x   --->  x / 16
    test(100, 10)
    #task_2_lab_1(200, 25)
    turtle.done()