import random
import turtle

swidth , sheight, psize , exit_count = 300, 300, 3, 0
r,g,b,angle, dist, curX, curY =[0]*7

turtle.shape('turtle')
turtle.pensize(psize)

turtle.setup(width=swidth+30, height=sheight+30,)
turtle.screensize(swidth,sheight)

while True:
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r,g,b))

    angle = random.randrange(0, 360)
    dist = random.randrange(1, 100)
    turtle.left(angle)
    turtle.forward(dist)
    curX = turtle.xcor();
    curY = turtle.ycor();

    if(curX>= -swidth/2 and curX<=swidth/2) and (curY >-sheight/2 and curY<=sheight/2):
        pass
    else:
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        exit_count+=1
        if exit_count>=5:
            break

turtle.done()