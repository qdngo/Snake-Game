#Snake Game by QuangDaoNgo
import turtle
import time
import random 

delay = 0.1

#Score
score = 0 
high_score = 0


#set up the screen
window = turtle.Screen()
window.title("Snake Game by @QuangDaoNgo") #game title
window.bgcolor("black") #background color
window.setup(width=600, height=600) #size of the screen
window.tracer(0) #turns of the screen updates

#create the snake head
head = turtle.Turtle()
head.speed(0) #set to 0 because it is the fastest animation, as fast as possible
head.shape("square") #set the head shape (it can be 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic')
head.color("white")
head.penup() #the python turtle is keeping drawing the line so using penup could stop drawing any line
head.goto(0,0) #start at the center of the screen
head.direction = "stop" #head going to seat there in the middle

#create the snake food
snakeFood = turtle.Turtle()
snakeFood.speed(0)  
snakeFood.shape("circle")
snakeFood.color("red")
snakeFood.penup()
snakeFood.goto(0,100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape = "square"
pen.color = "white"
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write("Score: 0   High Score Record: 0", align = "center", font = ("Courier", 24, "normal"))

#functions
def move_up():
    if head.direction != "down":
        head.direction == "up"
def move_down():
    if head.direction != "up":
        head.direction == "down"
def move_right():
    if head.direction != "left":
        head.direction == "right"
def move_left():
    if head.direction != "right":
        head.direction == "left"    

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


#keyboard bindings 
window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "d")
window.onkeypress(move_left, "a")


#main game loop
while True:
    window.update()  #everytime go through the loop, this update the screen

    #Check for the collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #Hide the segment
        for segment in segments:
            segment.goto(1000,1000)

        #Clear the segment list
        segments.clear()

        #Reset the score when start playing
        score.clear()

        #Reset the delay 
        delay = 0.1

        #Update the score
        pen.clear()
        pen.write("Score: {}   High Score Record: {}".format(score, high_score), align="center", font = ("Courier", 24, "normal"))

    if head.direction(snakeFood) < 20:
        #move the food after the snake reach it 
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        snakeFood.goto(x,y)

        #add a new segment for the snake when it eats the food
        snakeSegment = turtle.Turtle()
        snakeSegment.speed(0)
        snakeSegment.shape("square")
        snakeSegment.color("grey")
        snakeSegment.penup()
        segments.append(snakeSegment)

        #shorten the delay to increase the hard
        delay -= 0.001

        #increase the score when the snake eat the food
        score += 10
        if score > high_score:
            high_score = score
        #Update the score
        pen.clear()
        pen.write("Score: {}   High Score Record: {}".format(score, high_score), align="center", font = ("Courier", 24, "normal"))

    #move the end segments first in reverse order
    for index in range(len(segments)-1 , 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    #move the segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
  
    move()

    #check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #Hide the segment
            for segment in segments:
                segment.goto(1000,1000)

            #Clear the segment list
            segments.clear()
        
            #Reset the score when start playing
            score.clear()
            #Reset the delay
            delay = 0.1
            #Update the score
            pen.clear()
            pen.write("Score: {}   High Score Record: {}".format(score, high_score), align="center", font = ("Courier", 24, "normal"))

    time.sleep(delay)
    
  
#keep the window open
window.mainloop() 