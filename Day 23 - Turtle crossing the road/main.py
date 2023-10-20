import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.onkeypress(player.move_player, "Up")

game_is_on = True
is_ok = False
game_loop = 6

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.generate_cars()
    cars.move_cars()

    # Detect collision with cars
    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Check hitting finish line
    if player.check_finish_line():
        player.go_to_start()
        scoreboard.add_level()
        cars.speed_increase(scoreboard.score)


screen.exitonclick()
