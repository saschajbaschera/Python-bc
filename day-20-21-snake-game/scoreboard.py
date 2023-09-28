from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
with open("data.txt", mode="r") as file:
    CURRENT_HIGH_SCORE = file.read()


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(CURRENT_HIGH_SCORE)
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over.", align=ALIGNMENT, font=FONT)



