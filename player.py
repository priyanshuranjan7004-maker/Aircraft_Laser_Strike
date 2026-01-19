from turtle import Turtle

starting_position = (0,-280)
Move_distance =10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_to_start(self):
        self.goto(starting_position)
    def go_right(self):
        self.goto(self.xcor()+20,self.ycor())
        print("right sucess")
    def go_left(self):
        self.goto(self.xcor()-20,self.ycor())