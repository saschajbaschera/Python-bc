from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_level = 1
        self.penup()
        self.hideturtle()
        self.goto(-220, 260)
        self.write(f"Level: {self.player_level}", align="center", font=FONT)

    def add_level(self):
        self.clear()
        self.player_level += 1
        self.write(f"Level: {self.player_level}", align="center", font=FONT)
