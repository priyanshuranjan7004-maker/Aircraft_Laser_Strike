import random
import turtle
from obstacles import Obstacles

screen = turtle.Screen()
screen.setup(width=600,height=600)

t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.goto(0,-280)
t.shapesize(stretch_len=2,stretch_wid=2)

obstacles =Obstacles()

def move_forward():
    t.fd(50)
def turn_left():
    t.left(90)

screen.onkey(move_forward,"Up")
screen.onkey(turn_left,"Left")
screen.tracer(0)

while True:
    Obstacles()
    screen.listen()
    screen.mainloop()
    obstacles.create_obstacles()


