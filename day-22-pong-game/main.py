from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.setup(height=800, width=1200)
my_screen.bgcolor("black")
my_screen.title("Pong")
my_screen.tracer(0)

paddles = Paddle()
ball = Ball()
scoreboard = Scoreboard()

my_screen.listen()

my_screen.onkey(paddles.player_up, "Up")
my_screen.onkey(paddles.player_down, "Down")


game_is_on = True
enemy_heading = "down"

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    ball.move_ball()

    # Moving enemy paddle
    if enemy_heading == "down":
        paddles.enemy_paddle_down()
    if enemy_heading == "up":
        paddles.enemy_paddle_up()

    # Change enemy paddle orientation
    for segment in paddles.enemy_segments:
        ycor = segment.ycor()
        if ycor < -380:
            enemy_heading = "up"
        elif ycor > 380:
            enemy_heading = "down"

    # Bounce ball from player paddle
    for segment in paddles.player_segments:
        if ball.ball_segment[0].distance(segment) < 30:
            ball.player_bounce(ball.ball_segment[0].heading())

    # Bounce ball from enemy paddle
    for segment in paddles.enemy_segments:
        if ball.ball_segment[0].distance(segment) < 30:
            ball.enemy_bounce(ball.ball_segment[0].heading())

    # FOR TEST Bounce ball from enemy out and add score
    if ball.ball_segment[0].xcor() > 580:
        ball.enemy_bounce(ball.ball_segment[0].heading())
        scoreboard.score_update("player")
        ball.reset()

    # Ball in player out and add score
    if ball.ball_segment[0].xcor() < -580:
        scoreboard.score_update("enemy")
        ball.reset()

    # Bounce ball from top
    if ball.ball_segment[0].ycor() > 380:
        if ball.ball_segment[0].heading() > 90:
            ball.wall_bounce_top_from_right(ball.ball_segment[0].heading())
        else:
            ball.wall_bounce_top_from_left(ball.ball_segment[0].heading())

    # Bounce ball from bottom
    if ball.ball_segment[0].ycor() < -380:
        if ball.ball_segment[0].heading() > 270:
            ball.wall_bounce_bottom_from_left(ball.ball_segment[0].heading())
        else:
            ball.wall_bounce_bottom_from_right(ball.ball_segment[0].heading())

    if scoreboard.enemy_score_amount == 3:
        game_is_on = False
        scoreboard.player_score_object[0].goto(0, 0)
        scoreboard.player_score_object[0].write("Game over.", align="center", font=("Arial", 50, "normal"))

    elif scoreboard.player_score_amount == 3:
        game_is_on = False
        scoreboard.player_score_object[0].goto(0, 0)
        scoreboard.player_score_object[0].write("You've won.", align="center", font=("Arial", 50, "normal"))


my_screen.exitonclick()


