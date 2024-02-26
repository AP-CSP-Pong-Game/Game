import turtle as trtl 

playerscore = 0
font_setup = ("Arial", 20, "normal")
test = trtl.Turtle()
score_display = trtl.Turtle()
score_w = trtl.Turtle()


test.goto(0,0)
test.forward(1005)

x = test.xcor()
y = test.ycor()
if x >= 1000:
    playerscore = playerscore + 1
    score_display.penup()
    score_display.goto(0,450)
    score_display.hideturtle()
    score_display.pendown()
    score_w.penup()
    score_w.hideturtle()
    score_w.goto(-80, 450)
    score_w.pendown()
    score_w.write("Score:", font=font_setup)
    score_display.write(playerscore, font=font_setup)


if x <= 1000:
    score_display.penup()
    score_display.hideturtle()
    score_display.clear()
    score_display.goto(-50,450)
    score_display.pendown()
    score_display.write("Game Over", font=font_setup)



wn = trtl.Screen()
wn.mainloop()