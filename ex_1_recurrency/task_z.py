import turtle
from turtle import *

turtle.speed(20)
#Screen().tracer(0)

def trojkat(bok, ilosc):
    if ilosc == 0:
        return
    for i in range(3):
        forward(bok)
        left(120)
        left(180)
        trojkat(bok/2, ilosc - 1)
        right(180)



trojkat(250, 5)
turtle.done()



