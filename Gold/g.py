import turtle
import random
score=0
beach=turtle.Screen()
beach.bgpic("beach.gif")
beach.addshape("l.gif")
beach.addshape("r.gif")
beach.addshape("c.gif")

hunter=turtle.Turtle()
hunter.shape("r.gif")
hunter.penup()
hunter.goto(0,-150)

scoreboard=turtle.Turtle()
scoreboard.penup()
scoreboard.speed(500)
scoreboard.goto(-100,240)
scoreboard.write("Score : 0",font=("Arial",27,"bold"))
scoreboard.hideturtle()

coin=turtle.Turtle()
coin.speed(100)
coin.shape("c.gif")
coin.penup()
coin.goto(-280,280)


def right():
    hunter.shape("l.gif")
    hunter.forward(5)
def left():
    hunter.shape("r.gif")
    hunter.backward(5)

turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")

turtle.listen()
def move():
    y=coin.ycor()
    coin.sety(y-3)
    
while True:
    beach.update()
    move()
    if coin.ycor()<-300:
        x=random.randint(-280,280)
        coin.goto(x,280)
    if hunter.distance(coin)<50:
        score=score+1
        scoreboard.clear()
        scoreboard.write("score : {}".format(score),font=("Arial",27,"bold"))
        x=random.randint(-280,280)
        coin.goto(x,280)
turtle.done() 