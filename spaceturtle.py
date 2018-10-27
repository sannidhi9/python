def main():
    import turtle
    import math
    import random
    import os
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

    def restart():
        turtle.Screen().clear()
        main()





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
         p.setposition(-100,-100)
         g = "FINAL SCORE: %s" % score
         p.write(g, False, align="left", font=("Arial",24, "normal"))
         f=open("hs.txt",'r')
         t=f.read()
         f.close()
         if score>int(t):
                 open("hs.txt", 'w').close()
                 l=open("hs.txt", 'w')
                 l.write("%s" % score)
                 l.close()
                 p.setposition(-200,70)
                 p.color("yellow")
                 z = "CONGRAGULATIONS!!!!!\n NEW HIGH SCORE: %s" % score
                 p.write(z, False, align="left", font=("Arial",28, "normal"))

         p.setposition(-150,-130)
         e="press space to play again"
         p.color("purple")
         p.write(e, False, align="left", font=("Arial",20,"normal"))
         p.setposition(-70,-300)
         p.color("red")
         p.write("click to exit", False, align="left", font=("Arial",14, "normal"))
         f=turtle.Screen()
         f.exitonclick()






    turtle.listen()
    turtle.onkey(turnleft, "Left")
    turtle.onkey(turnryt, "Right")
    turtle.onkey(speedup, "Up")
    turtle.onkey(restart,"space")
    while True:
        plr.fd(speed)
        # boundry
        if plr.xcor() > 280 or plr.xcor() < -280:
            gameover()
            winsound.PlaySound("smash.wav", winsound.SND_ASYNC)
            break

        if plr.ycor() > 280 or plr.ycor() < -280:
            gameover()
            winsound.PlaySound("smash.wav", winsound.SND_ASYNC)
            break

        if iscollision(plr, food):
            food.setposition(random.randint(-265, 265), random.randint(-265, 265))
            score=score+1
            br.undo()
            br.penup()
            br.hideturtle()
            br.setposition(-290,300)
            s="SCORE: %s"%score
            br.write(s,False,align="left",font=("Arial",14,"normal"))
            winsound.PlaySound("jump.wav",winsound.SND_ASYNC)
            if score==50:
                spped=speed+1
            elif score==40:
                b.bgpic("p1.gif")
                winsound.PlaySound("powerup.wav",winsound.SND_ASYNC)
                speed=speed+0.50
            elif score==30:
                b.bgpic("p2.gif")
                winsound.PlaySound("powerup.wav", winsound.SND_ASYNC)
                speed = speed + 0.70
            elif score==20:
                b.bgpic("p3.gif")
                winsound.PlaySound("powerup.wav", winsound.SND_ASYNC)
                speed = speed + 0.40
            elif score==10:
                b.bgpic("p4.gif")
                winsound.PlaySound("powerup.wav", winsound.SND_ASYNC)
                speed = speed + 0.30
main()




