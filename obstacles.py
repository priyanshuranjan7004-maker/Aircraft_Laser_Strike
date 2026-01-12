# def obstacles(self):
import random as r
import turtle
import time
game = True

class Obstacles:
    def __init__(self):
        # time.sleep(3)
        self.turt_obst =turtle.Turtle()
        self.turt_obst.shape("square")
        self.turt_obst.shapesize(stretch_wid=1,stretch_len=2)
        self.turt_obst.penup()
        time.sleep(4)
