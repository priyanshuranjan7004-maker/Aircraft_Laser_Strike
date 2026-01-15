from turtle import Turtle
import random

COLORS = ["red","orange","yellow","green","blue","purple"]
STARTING_MOVING_DISTANCE = 5
class Obstacles:
    def __init__(self):
        self.all_obstacles =[]
        self.car_Speed = STARTING_MOVING_DISTANCE

    def create_obstacles(self):
        new_obstacle = Turtle("square")
        new_obstacle.shapesize(stretch_wid=2,stretch_len=1)
        new_obstacle.penup()
        new_obstacle.color(random.choice(COLORS))
        random_x = random.randint(-250,250)
        new_obstacle.goto(300,random_x)
        self.all_obstacles.append(new_obstacle)
    def move_obstacles(self):
        for car in self.all_obstacles:
            car.backward(self.car_Speed)

        # run()
