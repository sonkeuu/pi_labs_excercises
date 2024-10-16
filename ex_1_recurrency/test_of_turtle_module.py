from turtle import *
import turtle
from math import sqrt

turtle.speed(10)
screen = turtle.Screen()


def starting_position_square(set_distance):
    turtle.penup()
    turtle.goto(set_distance / 2, -(set_distance / 2))
    turtle.pendown()

def starting_position_triangle(set_distance):
    turtle.penup()
    turtle.goto(set_distance / 2, -(set_distance / 3))
    turtle.pendown()


def triangle(set_distance: int):

    for i in range(3):
        turtle.left(120)
        turtle.forward(set_distance)


def square(set_distance: int):

    for i in range(4):
        turtle.left(90)
        turtle.forward(set_distance)

