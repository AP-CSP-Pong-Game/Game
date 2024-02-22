#set up

import turtle as trtl
paddle = trtl

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

startx = 400
starty = -260
paddle.goto(startx,starty)

#-----countdown writer-----
counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(0, 300)
#-----game functions-----
import turtle as turtl
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#movement for player
def moveU():
    paddle.forward(10)
    
def moveD():
    paddle.back(10)
    


screen.onkeypress(moveU, "Up")
screen.onkeypress(moveD, "Down")
screen.listen()


screen.mainloop()