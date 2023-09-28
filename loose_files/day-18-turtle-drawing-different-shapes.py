from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")


def change_color():
    r = random.random()
    b = random.random()
    g = random.random()

    timmy.color(r, b, g)


def draw(angles):
    for _ in range(angles):
        timmy.forward(100)
        timmy.right(360/angles)


start_angles = 3
for _ in range(8):
    draw(start_angles)
    start_angles += 1
    change_color()





















screen = Screen()
screen.exitonclick()
