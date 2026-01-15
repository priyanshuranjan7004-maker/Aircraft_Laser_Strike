
from turtle import Turtle
import random

COLORS = ["red","orange","yellow","green","blue","purple"]
class Obstacles:
    def __init__(self):
        self.all_obstacles =[]

    def create_obstacles(self):
        new_obstacle = Turtle()
        new_obstacle.shapesize(stretch_wid=2,stretch_len=1)
        new_obstacle.penup()
        new_obstacle.color(random.choice(COLORS))
        random_x = random.randint(280,-280)
        self.goto(random_x,280)
        self.all_obstacles.append(new_obstacle)

        # run()
