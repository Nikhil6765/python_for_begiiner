import turtle as t
def rectangle(horizontal,vertical,color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()

    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)

    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
t.bgcolor('black')

#feet

t.goto(-100,-150)
rectangle(50,20,'blue')
t.goto(-30,-150)
rectangle(50,20,'blue')



#legs

t.goto(-25,-50)
rectangle(15,100,'grey')

t.goto(-70,-50)
rectangle(15,100,'grey')

#body

t.goto(-100,100)
rectangle(120,150,'red')

#leftarm

t.goto(-160,50)
rectangle(60,20,'grey')
t.goto(-160,75)
rectangle(15,25,'grey') 

# right arm
t.goto(20,50)
rectangle(60,20,'grey')
t.goto(65,75)
rectangle(15,25,'grey')

