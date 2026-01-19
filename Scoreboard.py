from turtle import Turtle

font_style = ("Arial", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        # self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(-280,270)
        self.color(1,1,1)
        print("hello")

        self.write("score:0",font = font_style)
    def update (self,sel):
        self.clear()
        self.write(f"score:{sel}",font=font_style)
    def close_window(self):
        self.clear()
        self.goto(-150,-50)
        self.write("GAME OVER",font=("Arial",40,"bold"))
