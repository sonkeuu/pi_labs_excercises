from turtle import *
import turtle
from test_of_turtle_module import starting_position_square
from test_of_turtle_module import square
from Shape_class import Shape

turtle.speed(8)
screen = turtle.Screen()


class Task_A1(Shape):

    def __init__(self, set_the_distance):
        self._distance = set_the_distance

    def shape_inside(self):

        #   starting_position_square(self._distance)
        #   square(self._distance)
        distance_2 = self._distance
        distance_2 = distance_2 / 2
        base_pos = (-distance_2 / 2, distance_2 * 3 / 4)

#   for j in range(1):
#   distance_2 = distance_2 / 2

        for i in range(4):
            turtle.penup()
            turtle.goto(0, 0)
            turtle.forward(distance_2)
            turtle.right(90)
            turtle.pendown()
            square(distance_2)

    def draw_the_shape(self):

        #   starting_position_square(self._distance)
        #   square(self._distance)
        base_position = (self._distance / 2, self._distance / 2)

        distance_2 = self._distance

        for j in range(4):
            distance_2 = distance_2 / 2
            turtle.penup()
            #   turtle.goto(base_position)
            #   turtle.position = (-(distance_2 / 4), 3 * distance_2 / 4)
            turtle.forward(-(distance_2 / 4))
            turtle.left(90)
            turtle.forward(3 * distance_2 / 4)

            starting_position_square(distance_2)
            square(distance_2)
            #   turtle.goto(base_position)

            turtle.right(90)
    def draw_again(self):

        for i in range(2):
            #   turtle.penup()
            turtle.forward(self._distance / 2)
            starting_position_square(self._distance)
            #   turtle.pendown()
            square(self._distance / 2)
            distance_2 = self._distance / 2
            turtle.goto(0,0)
            #   turtle.right(90)


def task_a1(x, min):
    if x < min:
        return
    for i in range(4):
        forward(x)
        left(180)
        task_a1(x/2, min)
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
