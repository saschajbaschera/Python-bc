from turtle import Turtle
import time

STARTING_POSITION_PLAYER = [(-580, 30), (-580, 10), (-580, -10), (-580, -30)]
STARTING_POSITION_ENEMY = [(570, 390), (570, 370), (570, 350), (570, 330)]


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.player_segments = []
        self.enemy_segments = []
        self.create_player_paddle()
        self.create_enemy_paddle()
        self.enemy_moving = True

    def create_enemy_paddle(self):
        for position in STARTING_POSITION_ENEMY:
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            self.speed("fastest")
            new_segment.penup()
            new_segment.goto(position)
            self.enemy_segments.append(new_segment)

    def create_player_paddle(self):
        for position in STARTING_POSITION_PLAYER:
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            self.speed("fastest")
            new_segment.penup()
            new_segment.goto(position)
            self.player_segments.append(new_segment)

    def player_up(self):
        for segment in self.player_segments:
            new_ycor = segment.ycor() + 20
            segment.goto((segment.xcor(), new_ycor))

    def player_down(self):
        for segment in self.player_segments:
            new_ycor = segment.ycor() - 25
            segment.goto((segment.xcor(), new_ycor))

    def enemy_paddle_up(self):
        for segment in self.enemy_segments:
            new_ycor = segment.ycor() + 25
            segment.goto((segment.xcor(), new_ycor))

    def enemy_paddle_down(self):
        for segment in self.enemy_segments:
            new_ycor = segment.ycor() - 20
            segment.goto((segment.xcor(), new_ycor))











