print("hello")

from turtle import *
import turtle

#   turtle.forward(100)
turtle.speed(4)


def starting_position_square(set_distance):
    turtle.penup()
    turtle.goto(-(set_distance/2), -(set_distance/2))
    turtle.pendown()


def starting_position_triangle(set_distance):
    turtle.penup()
    turtle.goto(-(set_distance/2), -(set_distance/3))
    turtle.pendown()


def triangle(set_distance: int):

    starting_position_triangle(set_distance)

    for i in range(3):
        turtle.left(120)
        turtle.forward(set_distance)


def square(set_distance: int):

    #starting_position_square(set_distance)

    for i in range(4):
        turtle.left(90)
        turtle.forward(set_distance)


class Shape:

    def draw_the_shape(self):
        ...


class Task_A1(Shape):

    def __init__(self, set_the_distance):
        self._distance = set_the_distance


    def shape_inside(self):


    def draw_the_shape(self):

        square(self._distance)
        distance_2 = self._distance

        for i in range(4):

            distance_2 = distance_2 / 2

            for j in range(4):

                turtle.left(90)
                square(distance_2)
                turtle.forward(self._distance)
                #turtle.penup()





screen = turtle.Screen()


#triangle(400)
#square(400)

Task_A1(300).draw_the_shape()

Screen().exitonclick()