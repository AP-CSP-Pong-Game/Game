#set up
import time
import turtle as trtl
paddle = trtl.Turtle()

#create screen
screen = trtl.Screen()
#give screen a title
screen.title("Pong game")
#sets the background color of the screen
screen.bgcolor("white")
#sets the width and height of the screen
screen.setup(width=800, height=600)

#paddle setup
paddle.penup()
paddle.left(90)

Pshape = "square"
Pcolor = "green"

paddle.shape(Pshape)
paddle.color(Pcolor)
paddle.shapesize(3)
paddle.fillcolor(Pcolor)

speed = 2

startx = 400
starty = -260
paddle.goto(startx,starty)

#BALL

#color
color = "black"
#Shape
Shape = "circle"
#Speed
Speed = 4
# this is declaring the ball
ball = trtl.Turtle()
#Setting the ball's shape
ball.shape(Shape)
#setting the ball's position
ball.setposition(0, 0)
#setting the ball's color
ball.color(color)
#setting the ball's speed
ball.speed(Speed)
#makes sure the turtle(ball) won't write anything
ball.penup()
dy = -5
dx = 5
ballYCord = ball.ycor
ballXCord = ball.xcor

#-----countdown variables-----
font_setup = ("Arial", 20, "normal")

timer_up = False

#-----countdown writer-----
counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(0,0)
start = time.time()

#-----game functions-----

#movement for player
def moveU():
    if paddle.position == (400,270):
      print("stoped")
    else:
      paddle.forward(speed)
    
    
def moveD():
    if paddle.position == (400,0):
      print("stoped")
    else:
      paddle.back(speed)

#Sets the ball's color   
def SetBallColor(str):
    color = str
    ball.color(color)

#function to set ball shape
def SetBallShape(str):
    Shape = str
    ball.shape(Shape)

#function to set ball speed
def SetBallSpeed(number):
    Speed = number
    ball.speed(Speed)

#function to get ball color
def GetBallColor():
    return color

#function to get ball shape
def GetBallShape():
    return Shape

#function to get ball speed
def GetBallSpeed():
    return Speed

#speed change
def speedchange():
  global speed
  if int((time.time() - start)) % 5 == 0:
     speed += 0.001
     paddle.speed(speed)
     #print("speed change")

screen.onkeypress(moveU, "Up")
screen.onkeypress(moveD, "Down")
screen.listen()

#wn = trtl.Screen()

screen.tracer(0)

#this is gnna get replaced with computer score
while True:
    speedchange()
    counter.clear()

    counter.write(int(time.time() - start), font = ("arial", 30))
    #movement of the ball
    ballYCord = ball.ycor
    ballXCord = ball.xcor
    ball.setx(ballXCord + dx) # crashing at this line
    ball.sety(ballYCord + dy)

    PlayerYCord = paddle.ycor
    PlayerXCord = paddle.xcor
    # y coord boarders for the ball
    if (ballYCord > 280):
        ball.sety(280)
        dy *=-1
    
    if (ballYCord < -280):
        ball.sety(-280)
        dy *= -1
    
    #scoring the ball
    if (ballXCord > 500):
        ball.setposition(0, 0)
        dy *= -1
        #computer gets a point here
    
    if (ballXCord < -500):
        ball.setposition(0, 0)
        dy *=-1
        #Player gets a point
    
    #computer hits the ball
    if (ballXCord < -360 and ballXCord > -370) and (ballYCord < 0 and ballYCord > 0): 
        "computer paddle y cord + 40"  #first zero
        "computer paddle y cord - 40"  #second zero
        ball.setx(-360)
        dx *= -1
    
    #player hits the ball
    if (ballXCord > 360 and ballXCord > 370) and (PlayerYCord + 40 < 0 and PlayerYCord - 40 > 0): 
        "player paddle y cord + 40"  #first zero
        "player paddle y cord - 40"  #second zero
        ball.setx(360)
        dx *= -1
    screen.update()
