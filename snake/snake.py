import turtle
import random

segment=[]
grass=turtle.Screen()
grass.bgpic("g.gif")
grass.addshape("up.gif")
grass.addshape("down.gif")
grass.addshape("right.gif")
grass.addshape("left.gif")
grass.addshape("b.gif")

snake=turtle.Turtle()
snake.penup()
snake.speed(3)
snake.setheading(90)
snake.goto(0,0)
snake.shape("up.gif")

food=turtle.Turtle()
food.penup()
food.color("red")
food.shape("circle")
food.speed(500)
food.goto(100,10)

pen=turtle.Turtle()
pen.penup()
pen.speed(500)
pen.hideturtle()
pen.goto(0,250)
pen.write("Score : 0",font=("Arial",27,"bold"))

def move():
    snake.forward(5)
    
def up():
    if snake.heading()!=270:
        snake.setheading(90)
        snake.shape("up.gif")
    
def down():
    if snake.heading()!=90:
        snake.setheading(270)
        snake.shape("down.gif")
    
def right():
    if snake.heading()!=180:
        snake.setheading(0)   
        snake.shape("right.gif")

def left():
    if snake.heading()!=0:
        snake.setheading(180)
        snake.shape("left.gif")
    
turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(right,"Right")
turtle.onkeypress(left,"Left")
turtle.listen()
score=0
while True:
    grass.update()
    
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290:
        grass.bgpic("end.gif")
        food.hideturtle()
    
    for i in segment:
        if i.distance(snake)<10:
            grass.bgpic("end.gif")
            food.hideturtle()
        
        
        
    if snake.distance(food)<5:
        x=random.randint(-285,285)
        y=random.randint(-285,285)
        food.setpos(x,y)
        score=score+1
        pen.clear()
        pen.write("Score : {}".format(score),font=("Arial",27,"bold"))
        body=turtle.Turtle()
        body.penup()
        body.shape("b.gif")
        body.speed(0)
        segment.append(body)
        
    for i in range(len(segment)-1,0,-1):
        x=segment[i-1].xcor()
        y=segment[i-1].ycor()
        segment[i].goto(x,y)        
        
    if len(segment)>0:
        x=snake.xcor()
        y=snake.ycor()
        segment[0].goto(x,y)    
    move()

 
turtle.done()