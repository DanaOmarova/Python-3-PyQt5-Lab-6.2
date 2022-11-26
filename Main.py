import turtle

ddd = turtle.Turtle()

def draw_ddd (left_or_right, angle, length):
    if left_or_right == 'right':
        ddd.right(angle)
    else: ddd.left(angle)
    ddd.forward(length)

def draw_turtle (left_or_right, angle, length):
        if left_or_right == "right":
            turtle.right(angle)
        else:
            turtle.left(angle)
        turtle.forward(length)

ddd.fillcolor('turquoise')
ddd.begin_fill()

draw_ddd("left",155,100)
draw_ddd("right",65,100)
draw_ddd("right",65,100)
draw_ddd("right",50,100)
draw_ddd("right",65,100)
draw_ddd("right",65,100)

ddd.end_fill()

ddd.fillcolor('turquoise')
ddd.begin_fill()

draw_ddd("right",115,40)
draw_ddd("left",65,60)
draw_ddd("right",65,60)
draw_ddd("right",65,60)
draw_ddd("right",50,60)
draw_ddd("right",65,60)
draw_ddd("right",65,60)

ddd.end_fill()

ddd.back(60)
draw_ddd("right",50,60)
draw_ddd("right",65,60)
ddd.back(60)
draw_ddd("left",115,60)
draw_ddd("right",115,60)
draw_ddd("left",65,40)
draw_ddd("right",130,100)
draw_ddd("right",50,100)
draw_ddd("right",130,40)

turtle.done()
