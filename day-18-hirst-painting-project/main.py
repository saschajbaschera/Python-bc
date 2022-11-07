# import colorgram
import turtle
from turtle import Turtle, Screen
import random
# colors = colorgram.extract('image.jpg', 30)
# palett = []
#
# for color in colors:
#     palett.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(palett)


def dot_line(x_posi, y_posi):
    timmy.setpos(x_posi, y_posi)
    for _ in range(10):
        color = random.choice(color_list)
        timmy.dot(20, color)
        timmy.forward(50)


color_list = [(132, 166, 204), (220, 148, 108), (197, 135, 148), (32, 41, 61), (163, 59, 49), (41, 106, 155), (141, 183, 162), (237, 211, 92), (148, 61, 68), (214, 83, 72), (35, 61, 56), (52, 111, 91), (170, 29, 33), (158, 33, 30), (234, 167, 158), (17, 97, 71), (52, 44, 48), (230, 161, 165), (171, 188, 220), (58, 52, 49), (184, 103, 113), (32, 60, 108), (107, 127, 159), (175, 200, 188), (35, 150, 209), (66, 66, 56)]
turtle.colormode(255)
timmy = Turtle()
timmy.penup()
timmy.speed(10)
timmy.hideturtle()

x_pos = -250
y_pos = -300

for _ in range(10):
    dot_line(x_pos, y_pos)
    y_pos += 50


screen = Screen()
screen.exitonclick()
