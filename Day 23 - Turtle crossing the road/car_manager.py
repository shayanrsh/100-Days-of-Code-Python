from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self, level):
        super().__init__()
        self.penup()
        self.shape("square")
        self.generate_cars()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.speed_increase(level)

    def generate_cars(self):
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-250, 250))

    def move_cars(self):
        self.backward(self.car_speed)

    def speed_increase(self, level):
        self.car_speed += MOVE_INCREMENT * level
