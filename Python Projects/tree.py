# Michael Wu (mvw5mf)
import turtle

def draw_tree (t, depth, size):
    if depth == 0:
        return

    t.forward(size)
    t.left(35)
    t.forward(size)
    draw_tree (t,depth-1,size)
    t.backward(size)
    t.right(35*2)
    t.forward(size)
    draw_tree (t,depth-1,size)
    t.backward(size)
    t.left(35)
    t.backward(size)


tom = turtle.Turtle()
tom.left(90)
tom.penup()
tom.back(150)
tom.pendown()
tom.speed("slowest")

draw_tree(tom,5,20)

turtle.done()