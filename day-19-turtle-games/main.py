from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_pos = -100

is_race_on = False

if user_bet:
    is_race_on = True

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.setpos(x=-230, y=y_pos)
    y_pos += 33
    all_turtles.append(new_turtle)


while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() >= 230:
            is_race_on = False

            if turtle.pencolor() == user_bet:
                print(f"you've won, the {turtle.pencolor()} turtle has won")

            else:
                print(f"You've, lost, the {turtle.pencolor()} turtle has won! ")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
