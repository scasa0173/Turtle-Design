
from design1 import *
import turtle

turtle.colormode(255)

bob=turtle.Turtle()

bob.speed(0)
turtle.bgcolor("aqua")


jump(bob,-850,-850)
for times in range(255):
    c = (255- times, 0, 255-times)
#This code is using the times code but reversing it, it starts off black but instead the (-)reverses it so that it starts off with magenta.
    bob.color(c)
    polygon(bob,4,1700 - times * 3)

jump(bob,-50,100)
for times in range(7):
    cool(bob,10)
    bob.penup()
    bob.forward(50)
    bob.pendown()
    bob.right(360/7)



locations = [ (550,250) , (550, -150), (-595, -150), (-595,250)]
# What the locations code does is that it repeats the code below, however it locates it at the location given above while doing the same shapes.

for loc in locations:
    jump(bob,loc[0],loc[1])
    for times in range(7):
        cool(bob,5)
        bob.forward(10)
        bob.right(360/7)
