from random import randrange
from turtle import *
import turtle
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
global score
score = 0
pen = turtle.Turtle()
pen.penup()
pen.goto(-120, 150)
pen.hideturtle()
pen.write("Score = 0", align = "center", font=("Courier", 24, "normal"))

def inside(xy):
    # Return true if xy within screen
    return -200 < xy.x < 200 and -200 < xy.y < 200

def tap(x, y):
    # Respond to screen tap
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def draw():
    # Draw ball and targets
    clear()

    for i in targets:
        goto(i.x, i.y)
        dot(20, "blue")

    if inside(ball):
        goto(ball.x, ball.y)
        dot(10, "red")
    update()

def move():
    # Move the ball and Targets

    if randrange(40) == 0: # Generating thew position
        y = randrange(-150, 150)
        i = vector(200, y)
        targets.append(i)
    
    for i in targets: # Move the blue balls in a straight line
        i.x -= 0.35
        i.y -= 0.14
     
    if inside(ball): # move your red ball
        speed.y -= 0.35
        ball.move(speed)
    
    dupe = targets.copy()
    targets.clear()

    for i in dupe: # hit the blue balls
        if abs(i - ball) > 9:
            targets.append(i)

        else:
            global score
            score += 1
            pen.clear()
            pen.write(f"Score = {score}", align = "center", font=("Courier", 24, "normal"))
    
    draw()

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle() # Hide the turtle
up() # method used to pull pen up from the screen
tracer(False) # wont trace the path of the turtle
onscreenclick(tap)
move()
done()