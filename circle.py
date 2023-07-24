import turtle as t

from itertools import cycle
colors=cycle(['red','orange','yellow','green','blue','purple'])
bgcolour=cycle(['black','blue','white'])

def circle(size,angle,shift):
    t.bgcolor(next(colors))
    t.pencolor(next(bgcolour))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    circle(size+5,angle+1,shift+1)



#t.bgcolor('black')
t.speed('fastest')
t.pensize(10)
circle(30,0,1)