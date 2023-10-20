import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

all_cars = []

player = Player()
scoreboard = Scoreboard()

screen.onkeypress(player.move_player, "Up")

game_is_on = True
is_ok = False
game_loop = 6

while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in all_cars:
        car.move_cars()
        if player.distance(car) < 30 and player.ycor() - car.ycor() <= 5:
            game_is_on = False
            scoreboard.game_over()

    # Check hitting finish line
    if player.check_finish_line():
        scoreboard.add_level()

    if game_loop % 6 == 0:
        all_cars.append(CarManager(scoreboard.score))
    game_loop += 1

screen.exitonclick()
