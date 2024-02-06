import turtle

road=turtle.Screen()
road.bgpic("track.gif")
road.addshape("red.gif")
road.addshape("blue.gif")

redcar=turtle.Turtle()
redcar.shape("red.gif")
redcar.setheading(90)
redcar.penup()
redcar.goto(-100,-240)

bluecar=turtle.Turtle()
bluecar.shape("blue.gif")
bluecar.setheading(90)
bluecar.penup()
bluecar.goto(100,-240)

def player1():
    redcar.forward(5)
def player2():
    bluecar.forward(5)
    

turtle.onkeypress(player1,"Up")
turtle.onkeypress(player2,"w")
turtle.listen()
while True:
    road.update()
    if redcar.pos()>(-100,200):
        road.bgpic("rw.gif")
    if bluecar.pos()>(100,200):
        road.bgpic("bw.gif")
        
turtle.done()