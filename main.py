import time
from turtle import Screen
from obstacles import Obstacles
from player import Player

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)


player = Player()
obstacles =Obstacles()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.left, "Left")

screen.onkey(player.right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    obstacles.create_obstacles()
    obstacles.move_obstacles()

screen.exitonclick()