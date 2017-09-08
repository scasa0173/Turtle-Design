def polygon(t,sides,distance):
    angle=360/sides
    t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.left(angle)
    t.end_fill()


def cool(t,num):
    sides = 10
    for c in ["orange","yellow", "aqua","blue", "magenta","pink","white","black"]:
# the "c" command does almost the same as "locations". Instead it repeats the code, but with different colors. The different colors are the ones inside the brakets.
        t.color(c)
        polygon(t, sides, sides*num)
        t.forward(5)
        sides -= 1

def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
