import turtle
import math
import random
score=0
import winsound
# bg screen
b = turtle.Screen()
b.bgcolor("black")
b.bgpic("giphy.gif")
# border
br = turtle.Turtle()
br.penup()
br.goto(-300, 300)
br.pendown()
br.width(4)
br.speed(10000)
br.color("blue")
for i in range(4):
    br.fd(600)
    br.rt(90)
br.hideturtle()
# create player
plr = turtle.Turtle()
plr.shapesize(2,2,4)
plr.shape("turtle")
plr.color("green")
plr.penup()
plr.speed(0)
speed = 1
# food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.setposition(random.randint(-295, 295), random.randint(-295, 295))


# keystrokes
def turnleft():
    plr.lt(90)


def turnryt():
    plr.rt(90)


def speedup():
    global speed
    speed = speed + 1


def slowdown():
    global speed
    speed = speed - 1


def iscollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False
#game over
def gameover():
     b.bgpic("blog-game-over.gif")
     plr.color("red")
     p=turtle.Turtle()
     p.color("blue")
     p.penup()
     p.hideturtle()
     p.setposition(-70,-100)
     g = "FINAL SCORE: %s" % score
     p.write(g, False, align="left", font=("Arial", 14, "normal"))

turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnryt, "Right")
turtle.onkey(speedup, "Up")
while True:
    plr.fd(speed)
    # boundry
    if plr.xcor() > 280 or plr.xcor() < -280:
        gameover()


    if plr.ycor() > 280 or plr.ycor() < -280:
        gameover()

    if iscollision(plr, food):
        food.setposition(random.randint(-265, 265), random.randint(-265, 265))
        score=score+1
        br.undo()
        br.penup()
        br.hideturtle()
        br.setposition(-290,300)
        s="SCORE: %s"%score
        br.write(s,False,align="left",font=("Arial",14,"normal"))
        speed=speed+0.10
        winsound.PlaySound("jump.wav",winsound.SND_ASYNC)

end = input("press enter to exit!!")
