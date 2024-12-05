import turtle
# Also we can create 2 turtle: E.g Pokey = turtle.Turtle()
slowpoke = turtle.Turtle()
slowpoke.shape('turtle')


def make_shape(t, sides):
    angle = 360/sides
    for i in range(0, sides):
        t.forward(100)
        t.right(angle)
make_shape(slowpoke, 5)


slowpoke.pencolor('blue')
slowpoke.penup()
slowpoke.setposition(-120, 0)
slowpoke.pendown()
slowpoke.circle(50)


slowpoke.pencolor('red')
slowpoke.penup()
slowpoke.setposition(120, 0)
slowpoke.pendown()
for i in range (5):
    slowpoke.forward(100)
    slowpoke.right(144)


turtle.mainloop()
