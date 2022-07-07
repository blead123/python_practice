import turtle as t
import random as random

## 거북이 한마리의 1차원 리스트
my_turtle, tx, ty, tcolor, tsize, tshape = [None] * 6
shape_list = []
player_turtles = []
swidth, sheight, = 500, 500

## 메인 코드
if __name__ == "__main__":
    t.title("turtle list application")
    t.setup(width=swidth + 50, height=sheight + 50)
    t.screensize(swidth, sheight)
    shape_list=t.getshapes()

    for i in range(0,100):
        random.shuffle(shape_list)
        my_turtle = t.Turtle(shape_list[0])
        tx=random.randrange(-swidth/2 , swidth/2)
        ty=random.randrange(-sheight/2, sheight/2)
        r= random.random(); g=random.random(); b= random.random()
        tsize = random.randrange(1,3)
        player_turtles.append([my_turtle,tx,ty,tsize,r,g,b])

    for tlist in player_turtles:
        my_turtle = tlist[0]
        my_turtle.color((tlist[4],tlist[5],tlist[6]))
        my_turtle.pencolor((tlist[4],tlist[5],tlist[6]))
        my_turtle.turtlesize(tlist[3])
        my_turtle.goto(tlist[1], tlist[2])
    t.done()
