from turtle import *
import turtle
from test_of_turtle_module import starting_position_square
from test_of_turtle_module import square
from Shape_class import Shape

turtle.speed(10)
screen = turtle.Screen()


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


if __name__ == '__main__':

    Task_A1(300).shape_inside()
