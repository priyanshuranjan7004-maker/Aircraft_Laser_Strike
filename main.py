import random
import turtle
from obstacles import Obstacles



op = 5

screen = turtle.Screen()
screen.setup(width=600,height=400)

def obstacle():
    enemy =Obstacles()
    return enemy



square_obstacles = obstacle()
Final_enemy =square_obstacles.turt_obst

t = turtle.Turtle()
t.shape("turtle")
t.penup()

t.goto(0,-200)
# t.pendown()

t.shapesize(stretch_len=2,stretch_wid=2)
def move_forward():
    t.fd(50)
def turn_left():
    t.left(90)

screen.onkey(move_forward,"Up")
screen.onkey(turn_left,"Left")

while op < 10:
    op+=1
    print(op)
    x_axis = random.randint(20,60)
    y_axis = random.randint(300,400)
    position_vector = turtle.Vec2D(x_axis, y_axis)
    print(position_vector)
    print("Okey")
    Final_enemy.goto(position_vector)
    screen.listen()
    screen.mainloop()