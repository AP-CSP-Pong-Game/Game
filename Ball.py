import turtle as trtl

#SCREEN

#create screen
screen = trtl.Screen()
#give screen a title
screen.title("Pong game")
#sets the background color of the screen
screen.bgcolor("white")
#sets the width and height of the screen
screen.setup(width=1000, height=600)

#BALL

#color
color = "white"
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
ball.dy = -5
ball.dx = 5
#function to set Ball color
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

while True: #going to be replaced with computer score is less than 3
    screen.update()

    #movement of the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor + ball.dy)

    # y coord boarders for the ball
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *=-1
    
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
    
    #scoring the ball
    if ball.xcor() > 500:
        ball.setposition(0, 0)
        ball.dy *= -1
        #computer gets a point here
    
    if ball.xcor < -500:
        ball.setposition(0, 0)
        ball.dy *=-1
        #Player gets a point
    
    #computer hits the ball
    if (ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < 0 and ball.ycor() > 0): 
        "computer paddle y cord + 40"  #first zero
        "computer paddle y cord - 40"  #second zero
        ball.setx(-360)
        ball.sx *= -1
    
    #player hits the ball
    if (ball.xcor() > 360 and ball.xcor() > 370) and (ball.ycor() < 0 and ball.ycor() > 0): 
        "player paddle y cord + 40"  #first zero
        "player paddle y cord - 40"  #second zero
        ball.setx(360)
        ball.sx *= -1
    