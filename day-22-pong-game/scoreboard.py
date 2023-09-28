from turtle import Turtle

FONT = ("Arial", 60, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score_amount = 0
        self.enemy_score_amount = 0
        self.player_score_object = []
        self.enemy_score_object = []
        self.player_score()
        self.enemy_score()
        self.score_update("update")


    def player_score(self):
        score = Turtle()
        score.color("white")
        score.penup()
        score.goto(-90, 320)
        score.hideturtle()
        self.player_score_object.append(score)

    def enemy_score(self):
        score = Turtle()
        score.color("white")
        score.penup()
        score.goto(90, 320)
        score.hideturtle()
        self.enemy_score_object.append(score)

    def score_update(self, scorer):
        if scorer == "player":
            self.player_score_amount += 1
            self.player_score_object[0].clear()
        if scorer == "enemy":
            self.enemy_score_amount += 1
            self.enemy_score_object[0].clear()
        if scorer == "update":
            pass

        self.player_score_object[0].write(f"{self.player_score_amount}", align="center", font=FONT)
        self.enemy_score_object[0].write(f"{self.enemy_score_amount}", align="center", font=FONT)






