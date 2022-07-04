import turtle
import random

def screenLeftClick(x, y):
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)

def screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x,y)

def screenMidClick(x, y):
    global r, g, b
    tsize = random.random(1, 10)
    turtle.shapesize(tsize)
    r = random.random()
    g = random.random()
    b = random.random()

pen_size = 10
r, g, b = 0.0, 0.0, 0.0

turtle.shape('turtle')
turtle.pensize(pen_size)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()

