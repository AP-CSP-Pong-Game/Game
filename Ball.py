import turtle as trtl

#color
color = "white"
#Shape
Shape = "circle"
# this is declaring the ball
ball = trtl.Turtle()
#Setting the ball's shape
ball.shape(Shape)
#setting the ball's position
ball.setposition(0, 0)
#setting the ball's color
ball.color(color)
#setting the ball's speed
ball.speed(4)

def SetBallColor(str):
    ball.color(str)

def SetBallShape(str):
    ball.shape(str)

def SetBallSpeed(number):
    ball.speed(number)
