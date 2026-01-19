import time
import turtle
import math
from obstacles import Obstacles
from player import Player
from Scoreboard import Scoreboard

Hit_Score = 0


player = Player()
obstacles =Obstacles()
lasers = []


def bullets():
   bull= turtle.Turtle()
   bull.penup()
   bull.shapesize(stretch_wid=1,stretch_len=1)
   bull.color(1,0,0)
   bull.setposition(player.xcor(),player.ycor())
   bull.setheading(90)
   bull.forward(20)
   # bull.pendown()
   bull.pensize(5)
   lasers.append(bull)

def move_lasers(las):
    las.forward(10)
    las.forward(10)


def destroy_obstacles(la, ob):
    for lase, obstacle in zip(la, ob):
        print(f"lase.xcor ={math.floor(lase.ycor())}")
        print(f"obstacle.xcor ={math.floor(obstacle.ycor())}")
    for obs in ob :
        for lase in la :
            if obs.ycor() in range(math.floor(lase.ycor())-20,math.floor(lase.ycor())+20):
                print("Y:Sucess")
                if obs.xcor() in range(math.floor(lase.xcor())-20, math.floor(lase.xcor())+20):
                    print("X:Sucess")
                    lase.hideturtle()
                    lase.color("black")
                    lase.setposition(310,310)
                    ob.remove(obs)
                    obs.setposition(-310,-310)
                    la.remove(lase)
                    global Hit_Score
                    Hit_Score+=1
                    score.update(Hit_Score)


screen = turtle.Screen()
screen.colormode(255)
score = Scoreboard()

screen.bgcolor(40,40,40)
screen.title("SPACE INVADERS")
screen.setup(width=600,height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.go_right, "Right")
screen.onkey(player.go_left, "Left")
screen.onkey(bullets,"space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    obstacles.create_obstacles()
    op =obstacles.move_obstacles()

    if op:
        game_is_on= False
        score.close_window()
    destroy_obstacles(lasers, obstacles.list())
    for laser in lasers:
        if laser.ycor() >= 301:
            lasers.remove(laser)
        move_lasers(laser)

screen.exitonclick()