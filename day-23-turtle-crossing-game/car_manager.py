from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.moving_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.cars = []
        self.create_car()

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.setheading(180)
        car.color(random.choice(COLORS))
        car.goto(300, random.randint(-250, 250))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.moving_speed)

    def reset_cars(self):
        self.moving_speed += MOVE_INCREMENT

