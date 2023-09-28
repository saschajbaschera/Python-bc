from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.color("coral")
timmy.shape("circle")
timmy.speed("fastest")



def change_color():
    r = random.random()
    b = random.random()
    g = random.random()

    timmy.color(r, b, g)


def draw(size_gap):
    for _ in range(int(360 / size_gap)):
        change_color()
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_gap)


draw(10)




screen = Screen()
screen.exitonclick()