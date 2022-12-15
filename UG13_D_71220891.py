import turtle

t = turtle.Turtle()

t.screen.bgcolor("pink")
t.pencolor("white")
t.pensize(20)
t.fillcolor("white")


t.backward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(30)
t.right(90)
t.forward(70)
#
t.left(90)
t.forward(45)
#
t.left(90)
t.forward(70)
#
t.right(90)
t.forward(25)
#
# t.begin_fill("white")
# t.screen.bgcolor("pink")
# t.pencolor("white")
#

t.up()
t.goto(-65, -200)
t.down()
t.left(90)
t.forward(40)
t.right(90)
t.forward(100)
t.right(90)
t.forward(40)
t.right(90)
t.forward(100)


# t.forward(50)
#
# t.right(90)
# t.forward(50)
#
# t.pensize(2)
# for i in range(2):
#     t.penup()
#     t.goto(i*180, 30)
#     t.pendown()
#     t.circle(50)


sc = turtle.Screen().exitonclick()
