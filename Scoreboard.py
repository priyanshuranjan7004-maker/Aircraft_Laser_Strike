from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(-295,300)
        self.color("blue")
        font_style = ("Arial",24,"bold")
