from myTurtle import *
import turtle

inStr = ''

swidth, sheight = 300, 300
tX,tY,tAngle,tSize = [0]*4

turtle.title("거북이 글자 쓰기(모듈버전)")
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight +50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.speed(1)

inStr = get_string()

for i in inStr:

    tx,ty,ta,ts = det_xyas(swidth,sheight)
    r,g,b = det_rgb()

    turtle.goto(tx,ty)
    turtle.left(ta)

    turtle.pencolor((r,g,b,))
    turtle.write(i,font = ("맑은 고딕", ts , "bold"))


turtle.done