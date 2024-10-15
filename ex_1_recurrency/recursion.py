import turtle
from turtle import *

shape("arrow")

#forward(100)
#left(100)
#forward(50)
#right(150)


def shape_1():
    i = 1

    forward(100)
    left(100)
    forward(50)
    right(150)


print(shape_1())


class Shape:

    def drawing_pattern(self):
        ...


class Square(Shape):

    def __init__(self, pen_color="green", pen_size=3):
        self._turtle = turtle.Turtle()
        self._turtle.color(pen_color)
        self._turtle.pensize(pen_size)

    def drawing_pattern(self):
        forward(100)
        right(200)


Screen().exitonclick()

if __name__ == '__main__':
    print(Square().drawing_pattern())
