import time
from turtle import Screen
from obstacles import Obstacles
from player import Player
from Bullets import Bullet

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)


player = Player()
obstacles =Obstacles()
Bullets = Bullet()


# bull = Bullets.create_bullets(self=)a
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")
screen.onkey(Bullets.create_bullets,"A")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    obstacles.create_obstacles()
    obstacles.move_obstacles()
    Bullets.move_forward()

screen.exitonclick()