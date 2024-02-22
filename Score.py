import turtle as trtl 

playerscore = 0
trtl.goto(0,0)

trtl.forward(1005)

x = trtl.xcor()
y = trtl.ycor()
if x >= 1000:
    playerscore = playerscore + 1
    print("Score:", playerscore)

if x <= -1000:
    print("Game Over")
    print("Your Score is", playerscore)



trtl.done()
