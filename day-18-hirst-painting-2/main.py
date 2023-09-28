import colorgram
import turtle as t
import random

colors = colorgram.extract('image.jpg', 30)

colors_list = [(132, 166, 204), (220, 148, 108), (197, 135, 148), (32, 41, 61), (163, 59, 49), (41, 106, 155),
               (141, 183, 162), (237, 211, 92), (148, 61, 68), (214, 83, 72), (35, 61, 56), (52, 111, 91),
               (170, 29, 33), (158, 33, 30), (234, 167, 158), (17, 97, 71), (52, 44, 48), (230, 161, 165),
               (171, 188, 220), (58, 52, 49), (184, 103, 113), (32, 60, 108), (107, 127, 159), (175, 200, 188),
               (35, 150, 209), (66, 66, 56)]


# for color in colors:
#     rgb = color.rgb
#     rgb_color = (rgb.r, rgb.g, rgb.b)
#     colors_list.append(rgb_color)

tim = t.Turtle()
tim.pensize(10)
tim.penup()
t.colormode(255)
tim.speed(0)
tim.hideturtle()


def hirst_painting():
    tim.setx(-200)
    y = -200
    tim.sety(y)
    for _ in range(10):
        for _ in range(10):
            tim.pencolor(random.choice(colors_list))
            tim.dot(20)
            tim.forward(50)
        tim.setx(-200)
        y += 50
        tim.sety(y)




hirst_painting()

my_screen = t.Screen()
my_screen.exitonclick()
