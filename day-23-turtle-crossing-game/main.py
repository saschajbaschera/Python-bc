import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "space")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move_cars()

    # Check if player reached finishline, increase car speed and reset player and add level
    if player.ycor() > 280:
        scoreboard.add_level()
        player.arrived_at_finish()
        car_manager.reset_cars()

    # Randomly generating a car
    if random.randint(0, 5) == 5:
        car_manager.create_car()

    # Detect collision
    for car in car_manager.cars:
        if player.distance(car) < 15:
            game_is_on = False
            scoreboard.goto(0, 0)
            scoreboard.write("Game over.", align="center", font=("Courier", 24, "normal"))


screen.exitonclick()