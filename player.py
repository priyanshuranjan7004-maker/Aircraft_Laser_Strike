from turtle import Turtle

starting_position = (0,-280)
Move_distance =10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_to_start(self):
        self.goto(starting_position)
    def go_up(self):
        self.forward(Move_distance)