import turtle as t

from itertools import cycle
colors=cycle(['red','orange','yellow','green','blue','purple'])


def circle(size):
    t.pencolor('red')
    t.circle(size)


t.bgcolor('black')
t.speed('fast')
t.pensize(4)
