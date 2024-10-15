import random
import turtle
import math

win_length = 500
win_height = 500

turtles = 5

turtle.screensize(win_length, win_height)

class racer(object):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.turt = turtle.Turtle()
        self.turt.shape("arrow")
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.setheading(90)

    def move(self):
        r = random.randrange(1,20)
        self.pos = (self.pos[0], self.pos[1] + r)
        self.turt.pendown()
        self.turt.forward(r)

    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.pos)

def start_the_game():
    tlist = []
    turtle.clearscreen()
    turtle.hideturtle()
    colors = ["red", "green", "blue", "yellow", "pink"]
    start = -(win_length/2) + 20
    for t in range(turtles):
        newposx = start + t * win_length // turtles
        tlist.append(racer(colors[t], (newposx, -230)))
        tlist[t].turt.showturtle()

    run = True
    while run:
        for t in tlist:
            t.move()





