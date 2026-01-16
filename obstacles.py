from turtle import Turtle
import random

COLORS = ["red","orange","yellow","green","blue","purple"]
STARTING_MOVING_DISTANCE = 2
class Obstacles:
    def __init__(self):
        self.all_obstacles =[]
        self.car_Speed = STARTING_MOVING_DISTANCE

    def create_obstacles(self):
        if random.randint(1,3)==2:
            new_obstacle = Turtle("square")
            new_obstacle.shapesize(stretch_wid=2,stretch_len=1)
            new_obstacle.penup()
            new_obstacle.setheading(270)
            new_obstacle.color(random.choice(COLORS))
            random_x = random.randint(-250,250)
            new_obstacle.goto(random_x,300)
            self.all_obstacles.append(new_obstacle)
    def move_obstacles(self):
        for car in self.all_obstacles:
            car.forward(self.car_Speed)

        # run()
