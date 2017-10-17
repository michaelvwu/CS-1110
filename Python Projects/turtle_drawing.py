# Michael Wu (mvw5mf)
import turtle
import random

# def draw_square(t,x,y):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     color = ["green", "red", "yellow", "orange", "pink", "cyan", "black"]
#
#     for i in range(4):
#      which_colors = random.randint(0, len(color)-1)
#      t.color(color[which_colors])
#      t.forward(100)
#      t.right(90)
#
# tom = turtle.Turtle()
# tom.speed("slow")
#
# draw_square(tom,150,150)
# draw_square(tom,-150,150)
# draw_square(tom,-150,-150)
# draw_square(tom,150,-150)


def draw_shape(t,x,y, sides, side_length):
    t.penup()
    t.goto(x, y)
    t.pendown()
    color = ["green", "red", "yellow", "orange", "pink", "cyan", "black"]
    t.begin_fill()

    for i in range(sides):
     which_colors = random.randint(0, len(color)-1)
     t.color(color[which_colors])
     t.forward(side_length)
     t.right(360/sides)

    t.end_fill()

tom = turtle.Turtle()
tom.pensize(3)
tom.speed("slow")

draw_shape(tom,100,100,3,200)
draw_shape(tom,125,100,4,50)


turtle.done()

