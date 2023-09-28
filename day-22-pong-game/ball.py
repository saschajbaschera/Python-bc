from turtle import Turtle
import random


BALL_STARTING_POSITION = (0, 0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_segment = []
        self.ball_heading = random.randint(120, 220)
        self.create_ball()
        self.ball_speed = 25

    def create_ball(self):
        new_segment = Turtle()
        new_segment.color("white")
        new_segment.shape("circle")
        new_segment.penup()
        new_segment.goto(BALL_STARTING_POSITION)
        new_segment.speed(8)
        new_segment.setheading(self.ball_heading)
        self.ball_segment.append(new_segment)

    def move_ball(self):
        self.ball_segment[0].setheading(self.ball_heading)
        self.ball_segment[0].forward(self.ball_speed)

    def player_bounce(self, input_heading):
        self.ball_speed += 1
        if input_heading > 180:
            off_angle = input_heading - 180
            output_heading = 360 - off_angle
            self.ball_heading = output_heading
        elif input_heading < 180:
            off_angle = 180 - input_heading
            output_heading = 0 + off_angle
            self.ball_heading = output_heading
        else:
            self.ball_heading = 0

    def enemy_bounce(self, input_heading):
        self.ball_speed += 1
        if input_heading < 90:
            output_heading = 180 - input_heading
            self.ball_heading = output_heading
        elif input_heading > 270:
            off_angle = 360 - input_heading
            output_heading = off_angle + 180
            self.ball_heading = output_heading
        else:
            self.ball_heading = 180

    def wall_bounce_top_from_right(self, input_heading):
        off_angle = 180 - input_heading
        output_heading = 180 + off_angle
        self.ball_heading = output_heading

    def wall_bounce_top_from_left(self, input_heading):
        output_heading = 360 - input_heading
        self.ball_heading = output_heading

    def wall_bounce_bottom_from_right(self, input_heading):
        off_angle = input_heading - 180
        output_heading = 180 - off_angle
        self.ball_heading = output_heading

    def wall_bounce_bottom_from_left(self, input_heading):
        output_heading = -(input_heading - 360)
        self.ball_heading = output_heading

    def reset(self):
        self.ball_heading = random.randint(100, 260)
        self.ball_segment[0].goto(0, 0)





