
def shape_inside(self):

    square(self._distance)
    distance_2 = self._distance

    distance_2 = distance_2 / 2

    for j in range(4):
        turtle.left(90)
        square(distance_2)
        turtle.forward(self._distance)
        # turtle.penup()


def draw_the_shape(self):

    for i in range(3):

        self.shape_inside()
        turtle.right(270)
        self._distance = self._distance / 2






        turtle.penup()
        turtle.goto(0, distance_2)
        turtle.right(90)
        turtle.pendown()
        square(distance_2)

        turtle.penup()
        turtle.goto(distance_2, distance_2)
        turtle.right(90)
        turtle.pendown()
        square(distance_2)

        turtle.penup()
        turtle.goto(distance_2, -distance_2)
        turtle.right(90)
        turtle.pendown()
        square(distance_2)