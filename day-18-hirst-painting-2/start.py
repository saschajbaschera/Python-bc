import turtle as t
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black", "gray"]
angles = [0, 90, 180, 270, 360]
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b

def spirale(radius, amount):
    heading = 0
    for _ in range(amount):
        tim.circle(radius)
        tim.setheading(heading)
        heading += 360 / amount
        tim.pencolor(random_color())


tim = t.Turtle()
tim.shape("turtle")
tim.pensize(2)
tim.speed(0)

spirale(200, 100)










my_screen = t.Screen()
my_screen.exitonclick()
