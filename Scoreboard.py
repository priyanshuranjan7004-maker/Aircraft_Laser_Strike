from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        # self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(-295,300)
        self.color(1,1,1)
        font_style = ("Arial",24,"bold")
        print("hello")

        self.write("score:0",font = ("Arial",24,"bold"))
    def update (self,sel):
        self.clear()
        self.write(f"score:{sel}")