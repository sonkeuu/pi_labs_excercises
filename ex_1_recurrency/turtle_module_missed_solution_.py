from turtle import *
import turtle
from turtle_module_testing_functions import starting_position_square
from turtle_module_testing_functions import square

turtle.speed(8)
screen = turtle.Screen()


from turtle import *
import turtle
from turtle_module_testing_functions import starting_position_triangle


class Shape:
    ...


class Task_A10(Shape):

    def __init__(self, set_the_distance_10):
        self._distance_10 = set_the_distance_10

    def shape_inside(self):

        starting_position_triangle(self._distance_10)
        distance_gap = 10

        for i in range(10):
            turtle.left(120)
            turtle.forward(self._distance_10 - distance_gap)

    def triangle_spiral(self):

        starting_position_triangle(self._distance_10)

        distance_spiral_gap = 10

        for i in range(30):
            turtle.left(120)
            distance_spiral_gap = distance_spiral_gap + 10
            turtle.forward(self._distance_10 - distance_spiral_gap)


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


if __name__ == '__main__':

    #   Task_A1(300).shape_inside()

    #   task_1_lab_1(270, 10)
    task_2_lab_1(256, 128)
    turtle.done()
