import turtle as t

tim = t.Turtle()
my_screen = t.Screen()
tim.speed(10)


def move_forward():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def move_right():
    tim.right(20)


def move_left():
    tim.left(20)


def clear():
    my_screen.resetscreen()


my_screen.listen()
my_screen.onkey(move_forward, "w")
my_screen.onkey(move_backwards, "s")
my_screen.onkey(move_left, "a")
my_screen.onkey(move_right, "d")
my_screen.onkey(clear, "c")


my_screen.exitonclick()
