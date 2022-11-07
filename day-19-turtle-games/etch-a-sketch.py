from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def move_counter_clock():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def move_clock():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def clear():
    timmy.home()
    timmy.clear()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_counter_clock, "a")
screen.onkey(move_clock, "d")
screen.onkey(move_backwards, "s")
screen.onkey(key="c", fun=clear)

screen.exitonclick()