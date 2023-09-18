import turtle
import time
import random

posponer = 0.1

#marcador
score = 0
highscore = 0

#SnakeTable
SnakeTable = turtle.Screen()
SnakeTable .title("Snake game")
SnakeTable .bgcolor('Blue')
SnakeTable.setup(width = 600, height = 600)
SnakeTable.tracer(0)

#Head
Head = turtle.Turtle()
Head.shape('square')
Head.speed(0)
Head.color('Pink')
Head.penup()
Head.goto(0 , 0)
Head.direction = 'stop'

 #Box
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

#Comida
Food= turtle.Turtle()
Food.shape('circle')
Food.speed(0)
Food.color('red')
Food.penup()
Food.goto(0 , 100)

#Segmentos
segments = []

#Texto
Texto = turtle.Turtle()
Texto.speed(0)
Texto.color('white')
Texto.penup()
Texto.hideturtle()

#Funciones
def arriba():
    Head.direction = 'up'
def abajo():
    Head.direction = 'down'
def izquierda():
    Head.direction = 'left'
def derecha():
    Head.direction = 'right'

def  texto():
    Texto.clear()
    Texto.goto(0,260)
    Texto.color('white')
    Texto.write('Score: {}   High Score:  {}' .format(score,highscore),
                    align ='center', font = ('Courier', 24, 'normal'))
    #Texto.color('black')
    #Texto.goto(0,245)
    #Texto.write('----------------------------------------------------------------------------------------------------------------', align ='center', font = ('Courier', 20, 'normal'))

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
SnakeTable.onkeypress(arriba, "Up")
SnakeTable.onkeypress(abajo, 'Down')
SnakeTable.onkeypress(izquierda, 'Left')
SnakeTable.onkeypress(derecha, 'Right')

while True:
    SnakeTable.update()
    texto()


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
        texto()

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
            
        texto()

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
            texto()
        
    time.sleep(posponer)
    
    
