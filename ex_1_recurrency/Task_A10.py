from turtle import *
import turtle
from test_of_turtle_module import starting_position_triangle
from Shape_class import Shape


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
