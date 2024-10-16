print("hello")

from turtle import *
import turtle
from math import sqrt

#   turtle.forward(100)
turtle.speed(10)


def starting_position_square(set_distance):
    turtle.penup()
    turtle.goto(set_distance / 2, -(set_distance / 2))
    turtle.pendown()


def starting_position_triangle(set_distance):
    turtle.penup()
    turtle.goto(set_distance / 2, -(set_distance / 3))
    turtle.pendown()


def triangle(set_distance: int):
    #starting_position_triangle(set_distance)

    for i in range(3):
        turtle.left(120)
        turtle.forward(set_distance)


def square(set_distance: int):
    #starting_position_square(set_distance)

    for i in range(4):
        turtle.left(90)
        turtle.forward(set_distance)


class Shape:

    def shape_inside(self):
        ...

    def draw_the_shape(self):
        ...


class Task_A1(Shape):

    def __init__(self, set_the_distance):
        self._distance = set_the_distance

    def shape_inside(self):

        starting_position_square(self._distance)
        #square(self._distance)
        distance_2 = self._distance

        for j in range(4):
            distance_2 = distance_2 / 2

            for i in range(4):
                turtle.penup()
                turtle.goto(0, 0)
                turtle.forward(distance_2)
                turtle.right(90)
                turtle.pendown()
                square(distance_2)

    def draw_the_shape(self):

        for i in range(2):
            distance_3 = self._distance
            distance_3 = distance_3 / 2
            Task_A1(distance_3).shape_inside()


class Task_A10(Shape):

    def __init__(self, set_the_distance_10):
        self._distance_10 = set_the_distance_10

    def shape_inside(self, distance_spiral_gap: int):

        starting_position_triangle(self._distance_10)
        self._distance_spiral_gap = distance_spiral_gap

        for i in range(10):
            turtle.left(120)
            turtle.forward(self._distance_10 - self._distance_spiral_gap)






    def triangle_spiral(self):

        starting_position_triangle(self._distance_10)

        distance_spiral_gap = 10

        for i in range(30):
            turtle.left(120)
            distance_spiral_gap = distance_spiral_gap + 10
            turtle.forward(self._distance_10 - distance_spiral_gap)



class Task_A2(Shape):

    def __init__(self):
        ...





screen = turtle.Screen()

if __name__ == '__main__':
    #triangle(400)
    #square(400)

    Task_A1(300).shape_inside()

