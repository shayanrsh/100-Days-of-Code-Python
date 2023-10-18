import turtle
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for seg_position in STARTING_POSITION:
            tim = Turtle(shape="square")
            tim.color("white")
            tim.pu()
            tim.goto(seg_position)
            self.snake.append(tim)

    def move_forward(self):
        for snake_parts in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_parts - 1].xcor()
            new_y = self.snake[snake_parts - 1].ycor()
            self.snake[snake_parts].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    # def snake_control(self):
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)