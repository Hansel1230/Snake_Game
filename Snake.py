import turtle
import time
import random

#Scoreboard
score = 0
highscore = 0

#SnakeTable
SnakeTable = turtle.Screen()
SnakeTable .title("Snake game")
SnakeTable .bgcolor('Blue')
SnakeTable.setup(width = 600, height = 600)
SnakeTable.tracer(0)

#Snake table Box
Box = turtle.Turtle()
Box.penup()
Box.pensize(5)
Box.setpos(-295 , 260)
Box.pendown()
Box.fd(584)
Box.rt(90)
Box.fd(550)
Box.rt(90)
Box.fd(586)
Box.rt(90)
Box.fd(550)

#Head
Head = turtle.Turtle()
Head.shape('square')
Head.speed(0)
Head.color('Pink')
Head.penup()
Head.goto(0 , 0)
Head.direction = 'stop'

#Food
Food= turtle.Turtle()
Food.shape('circle')
Food.speed(0)
Food.color('red')
Food.penup()
Food.goto(0 , 100)

#segments
segments = []

#Text
Textturtle = turtle.Turtle()
Textturtle.speed(0)
Textturtle.color('white')
Textturtle.penup()
Textturtle.hideturtle()

#Functions
def up():
    Head.direction = 'up'
def down():
    Head.direction = 'down'
def left():
    Head.direction = 'left'
def right():
    Head.direction = 'right'

def Text():
    Textturtle.clear()
    Textturtle.goto(0,260)
    Textturtle.color('white')
    Textturtle.write('Score: {}   High Score:  {}' .format(score,highscore),
                    align ='center', font = ('Courier', 24, 'normal'))
    
def mov():
    if Head.direction == 'up':
        y = Head.ycor()
        Head.sety(y + 10)

    if Head.direction == 'down':
        y = Head.ycor()
        Head.sety(y - 10)

    if Head.direction == 'left':
         x = Head.xcor()
         Head.setx(x - 10)

    if Head.direction == 'right':
         x = Head.xcor()
         Head.setx(x + 10)
         
#Keyboard
SnakeTable.listen()
SnakeTable.onkeypress(up, "Up")
SnakeTable.onkeypress(down, 'Down')
SnakeTable.onkeypress(left, 'Left')
SnakeTable.onkeypress(right, 'Right')


while True:
    SnakeTable.update()
    Text()

    #Collision with the edge
    if Head.xcor() > 278 or Head.xcor() < - 280 or Head.ycor() > 240 or Head.ycor() < - 278:
        time.sleep(1)
        Head.goto(0,0)
        Head.direction = 'stop'
        Food.goto(0,100)

        #Hide Segments
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()

        score = 0
        Text()

    #Food collisions
    if Head.distance(Food) <20:
        x = random.randint(-280,280)
        y = random.randint(-280,240)
        Food.goto(x,y)

        #Segments
        newsegment = turtle.Turtle()
        newsegment.shape('square')
        newsegment.speed(0)
        newsegment.color('grey')
        newsegment.penup()
        
        #Add new segment
        segments.append(newsegment)

        #Increase bookmark
        score +=10

        if score >  highscore:
            highscore = score
            
        Text()

    #Move snake body
    TotalSeg = len(segments)
    for index in range(TotalSeg -1,0,-1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)

    if TotalSeg > 0:
        x = Head.xcor()
        y = Head.ycor()
        segments[0].goto(x,y)
        
    mov()

    #Collision with the body
    for segment in segments:
         if segment.distance(Head) < 10:
            time.sleep(1)
            Head.goto(0,0)
            Head.direction = 'stop'
            Food.goto(0,100)

            #Hide Segments
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()

            score = 0
            Text()
        
    time.sleep(0.1)
