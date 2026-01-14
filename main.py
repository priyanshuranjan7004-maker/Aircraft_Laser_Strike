import random
import turtle
from obstacles import Obstacles
Game = True

screen = turtle.Screen()
screen.setup(width=600,height=400)

def obstacle():
    enemy =Obstacles()
    return enemy

square_obstacles = obstacle()
Final_enemy1 =square_obstacles.turt_obst
Final_enemy2 = square_obstacles.turt_obst
Final_enemy3 = square_obstacles.turt_obst



t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.goto(0,-200)
t.shapesize(stretch_len=2,stretch_wid=2)

def move_forward():
    t.fd(50)
def turn_left():
    t.left(90)

screen.onkey(move_forward,"Up")
screen.onkey(turn_left,"Left")

while True:
    x_axis = random.randint(20,60)
    y_axis = random.randint(300,400)
    position_vector = (x_axis, y_axis)
    def position_vector(x,y):
        return [x,y]
    print("Okey")
    position =position_vector(x_axis,y_axis)
    # Final_enemy1.goto(position)
    position1 =[35,350]
    position2 = [55,320]
    Final_enemy2.goto(position1)
    Final_enemy3.goto(position2)
    screen.listen()
    screen.mainloop()



