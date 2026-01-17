import time
import turtle
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


screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.tracer(0)


# bull = Bullets.create_bullets(self=)a
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
    for laser in lasers:
        move_lasers(laser)
    # for laser in lasers and for obs in obstacles:
    #     if laser.po

    print(lasers)
    # print(obstacles.xcor())



    print(player.pos())


screen.exitonclick()