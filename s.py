import turtle
rocket=turtle.Turtle()
space=turtle.Screen()
astronaut=turtle.Turtle()

space.bgpic("maze.gif")
space.addshape("l.gif")
space.addshape("r.gif")
space.addshape("d.gif")
space.addshape("astronaut.gif")
astronaut.shape("astronaut.gif")
astronaut.penup()
astronaut.goto(-100,250)

space.addshape("rocket.gif")
rocket.shape("rocket.gif")
rocket.penup()
rocket.goto(180,-250)

def up():
    rocket.setheading(90)
    rocket.forward(10)
    rocket.setheading(0)
    rocket.shape("rocket.gif")
    
def down():
    rocket.setheading(270)
    rocket.forward(10)
    rocket.setheading(0)
    rocket.shape("d.gif")

def left():
    rocket.setheading(180)
    rocket.forward(10)
    rocket.setheading(0)
    rocket.shape("l.gif")

def right():
    rocket.forward(10)
    rocket.shape("r.gif")

turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.listen()


while True:
    space.update()
    if rocket.distance(astronaut)<10:
        space.bgpic("accomplishment.gif")
turtle.done()