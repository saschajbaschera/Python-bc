import turtle as t
import random

game_is_on = False
my_screen = t.Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []
y_start = -120

for color in colors:
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-y_start)
    y_start += 40
    new_turtle.color(color)
    all_turtles.append(new_turtle)


if user_bet:
    game_is_on = True

while game_is_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game_is_on = False

            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won, the {winning_color} turtle has won the game!")
            else:
                print(f"You've lost, the {winning_color} turtle has won the game!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




my_screen.exitonclick()
