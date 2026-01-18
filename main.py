import time
import turtle
import math
# from turtle import Screen
from obstacles import Obstacles
from player import Player


player = Player()
obstacles =Obstacles()
lasers = []


def bullets():
   bull= turtle.Turtle()
   bull.penup()
   bull.color(1,0,0)
   bull.setposition(player.xcor(),player.ycor())
   bull.setheading(90)
   bull.forward(20)
   bull.pendown()
   bull.pensize(5)
   lasers.append(bull)

def move_lasers(lasers):
    lasers.clear()
    lasers.forward(10)
    lasers.forward(10)


def destroy_obstacles(lasers,obstacles):
    for lase, obstacle in zip(lasers,obstacles):
        print(f"lase.xcor ={math.floor(lase.ycor())}")
        print(f"obstacle.xcor ={math.floor(obstacle.ycor())}")
    for obs in obstacles :
        for lase in lasers :
            if obs.ycor() in range(math.floor(lase.ycor())-15,math.floor(lase.ycor())+15):
                print("Y:Sucess")
                if obs.xcor() in range(math.floor(lase.xcor())-15, math.floor(lase.xcor())+15):
                    print("X:Sucess")
                    lasers.remove(lase)
                    lase.hideturtle()
                    lase.penup()

                    lase.setposition(310,310)
                    obstacles.remove(obs)
                    obs.setposition(-310,-310)

screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.tracer(0)


screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_left, "Left")
screen.onkey(bullets,"space")




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    obstacles.create_obstacles()
    obstacles.move_obstacles()
    destroy_obstacles(lasers, obstacles.list())
    for laser in lasers:
        if laser.ycor() >= 301:
            lasers.remove(laser)
        move_lasers(laser)


    print(lasers)
    print(player.pos())


screen.exitonclick()