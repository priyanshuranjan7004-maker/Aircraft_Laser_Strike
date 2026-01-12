# def obstacles(self):
import random as r
import turtle
import time
game = True

class Obstacles:
    def __init__(self,turt_obst):
        time.sleep(3)
        self.turt_obst =turtle.Turtle()
        self.turt_obst.shape("square")
        self.turt_obst.shapesize(stretch_wid=2,stretch_len=2)
        time.sleep(4)
        x= r.randint(100,-10)
        self.turt_obst.goto(x,y=200)
        self.turt_obst.down(1)
        # run()
