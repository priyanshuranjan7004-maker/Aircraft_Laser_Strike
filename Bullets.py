from turtle import Turtle
from player import Player
BULLET_SPEED = 4

class Bullet():

    def __init__(self):
        self.bulet = []
        self.BULLET_SPEED = BULLET_SPEED

    def create_bullets(self):
        bullet = Turtle("rectangle")
        bullet.shapesize(stretch_len=1,stretch_wid=1)
        bullet.goto(0,0)
        self.bulet.append(bullet)

    def move_forward(self):
        for b in self.bulet:
            b.forward(self.BULLET_SPEED)
