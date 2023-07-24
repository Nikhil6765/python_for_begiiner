import turtle as t

from itertools import cycle
colors=cycle(['red','orange','yellow','green','blue','purple'])


def circle(size):
    t.pencolor(next(colors))
    t.circle(size)
    circle(size+5)



t.bgcolor('black')
t.speed('fast')
t.pensize(4)
circle(30)