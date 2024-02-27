#set up
import time

import turtle as trtl
paddle = trtl.Turtle()

screen = trtl.Screen()
screen.setup(800,600)


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
    paddle.forward(speed)
    
def moveD():
    if paddle.position != (400,-260):
      paddle.back(speed)
    
#speed change
    
def speedchange():
  global speed
  if int((time.time() - start)) % 6 == 0:
     speed += 0.0001
     paddle.speed(speed)
     print("speed change")

screen.onkeypress(moveU, "Up")
screen.onkeypress(moveD, "Down")
screen.listen()

wn = trtl.Screen()

wn.tracer(0)

#this is gnna get replaced with computer score
while True:
  speedchange()
  counter.clear()

  counter.write(int(time.time() - start), font = ("arial", 30))
  wn.update()



