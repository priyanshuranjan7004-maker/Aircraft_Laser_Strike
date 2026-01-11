import turtle
from obstacles import Obstacles

screen = turtle.Screen()
screen.setup(width=600,height=400)

obs_s = turtle.Turtle()

enemy =Obstacles(obs_s)

# enemy.

t = turtle.Turtle()
t.shape("turtle")
t.penup()

t.goto(0,-200)
t.pendown()

def move_forward():
    t.fd(50)
def turn_left():
    t.left(90)

screen.onkey(move_forward,"Up")
screen.onkey(turn_left,"Left")

screen.listen()
screen.mainloop()