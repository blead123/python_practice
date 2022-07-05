import turtle as t

swidth, sheight = 500, 500
t.shape('turtle')
t.title("drawing rainbow circle")
t.setup(swidth+50, swidth+50)
t.screensize(swidth,swidth)
t.penup()
t.goto(-2,-sheight/2)
t.pendown()
t.speed(10)

for radius in range(1,250):
    if radius % 7 == 0:
        t.pencolor('red')
    if radius % 7 == 1:
        t.pencolor('blue')
    if radius % 7 == 2:
        t.pencolor('yellow')
    if radius % 7 == 3:
        t.pencolor('green')
    if radius % 7 == 4:
        t.pencolor('purple')
    if radius % 7 == 5:
        t.pencolor('navyblue')
    if radius % 7 == 6:
        t.pencolor('orange')
    t.circle(radius)
t.done


